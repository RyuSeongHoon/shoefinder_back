import re

NAME_PATTERN = r'([^[\]]+)(?:((?:\[[^[\]]+\])+)?(\[\])?)?$'
PATH_ELEMENTS_PATTERN = r'(?:\[(.+?)\])'

_match_name_format = re.compile(NAME_PATTERN).match
_parse_path_elements = re.compile(PATH_ELEMENTS_PATTERN).findall


def parse(data):
    result = {}

    for name, value in data.items():
        name_match = _match_name_format(name)
        if not name_match:
            raise ValueError(
                'Query string attribute in unknown format: %s' % name
            )
        base_name, path_elements, array_hint = name_match.groups()

        if path_elements:
            path_elements = _parse_path_elements(path_elements)
            path = result.setdefault(base_name, {})
            for path_element in path_elements[:-1]:
                path = path.setdefault(path_element, {})
            final_element = path_elements[-1]
        else:
            path = result
            final_element = base_name

        if not isinstance(path, dict):
            raise ValueError(
                "Mismatched type of string and mapping at %s" % name
            )

        if final_element in path:
            existing_value = path[final_element]
            if isinstance(existing_value, list):
                existing_value.append(value)
            else:
                path[final_element] = [existing_value, value]
        else:
            path[final_element] = [value] if array_hint else value

    return result
