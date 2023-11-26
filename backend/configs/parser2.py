import json
from configs import Configs
from configs import AugmentationConfig

schema = Configs.model_json_schema()
# print(schema)


def parse_json_schema(schema):
    result = {}

    def parse_object(obj):
        parsed_obj = {}

        if 'properties' in obj:
            for prop_name, prop_details in obj['properties'].items():
                parsed_obj[prop_name] = parse_property(prop_details)

        return parsed_obj

    def parse_property(prop):
        parsed_prop = {}

        if '$ref' in prop:
            ref_name = prop['$ref'].split('/')[-1]
            parsed_prop = parse_object(schema['$defs'][ref_name])

        elif 'properties' in prop:
            parsed_prop = parse_object(prop)

        elif 'type' in prop:
            parsed_prop = prop
            # parsed_prop['type'] = prop['type']

            # if 'title' in prop:
            #     parsed_prop['title'] = prop['title']

            # if 'minimum' in prop:
            #     parsed_prop['minimum'] = prop['minimum']

            # if 'maximum' in prop:
            #     parsed_prop['maximum'] = prop['maximum']

        return parsed_prop

    for prop_name, prop_details in schema['properties'].items():
        result[prop_name] = parse_property(prop_details)

    return result


parsed_schema = parse_json_schema(schema)
# category = 'train_config'
# category = 'network_config'
category = 'augmentation_config'
print(parsed_schema[category])
for key, val in parsed_schema[category].items():
    print(key, val)
# print(parsed_schema['network_config'])
# print(parsed_schema['augmentation_config'])

# print(parsed_schema)
