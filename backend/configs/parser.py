import json
from configs import Configs
from configs import AugmentationConfig

schema = {'TrainConfig': {'properties': {'device': {'fronzen': True, 'title': 'Device', 'type': 'string'
            }, 'device_ids': {'anyOf': [
                    {'type': 'integer'
                    },
                    {'type': 'string'
                    }
                ], 'fronzen': True, 'title': 'Device Ids'
            }, 'epochs': {'fronzen': True, 'title': 'Epochs', 'type': 'integer'
            }, 'batch_size': {'fronzen': True, 'title': 'Batch Size', 'type': 'integer'
            }, 'optimizer': {'fronzen': True, 'title': 'Optimizer', 'type': 'string'
            }, 'ml_framework': {'fronzen': True, 'title': 'Ml Framework', 'type': 'string'
            }, 'image_loading_lib': {'fronzen': True, 'title': 'Image Loading Lib', 'type': 'string'
            }, 'image_loading_mode': {'fronzen': True, 'title': 'Image Loading Mode', 'type': 'string'
            }, 'amp': {'default': False, 'fronzen': True, 'title': 'Amp', 'type': 'boolean'
            }, 'patience': {'default': 0, 'fronzen': True, 'title': 'Patience', 'type': 'integer'
            }, 'freeze': {'default': 0, 'metadata': {'description': 'how many layers you want to freeze'
                }, 'title': 'Freeze', 'type': 'integer'
            }, 'seed_model': {'anyOf': [
                    {'type': 'string'
                    },
                    {'type': 'null'
                    }
                ], 'default': None, 'fronzen': True, 'title': 'Seed Model'
            }, 'loss_fn': {'title': 'Loss Fn', 'type': 'string'
            }, 'focal_loss': {'title': 'Focal Loss', 'type': 'boolean'
            }, 'use_multiprocessing': {'default': False, 'title': 'Use Multiprocessing', 'type': 'boolean'
            }, 'workers': {'default': 8, 'title': 'Workers', 'type': 'integer'
            }, 'max_queue_size': {'default': 32, 'title': 'Max Queue Size', 'type': 'integer'
            }, 'bg_weights': {'anyOf': [
                    {'items': {'type': 'number'
                        }, 'type': 'array'
                    },
                    {'type': 'string'
                    },
                    {'type': 'null'
                    }
                ], 'default': None, 'title': 'Bg Weights'
            }, 'bg_weights_applied_epoch': {'anyOf': [
                    {'items': {'type': 'integer'
                        }, 'type': 'array'
                    },
                    {'type': 'string'
                    },
                    {'type': 'null'
                    }
                ], 'default': None, 'title': 'Bg Weights Applied Epoch'
            }, 'annotation_format': {'const': 'labelme', 'title': 'Annotation Format'
            }, 'dataset_type': {'enum': ['iter', 'iterable'
                ], 'title': 'Dataset Type', 'type': 'string'
            }
        }, 'required': ['device', 'device_ids', 'epochs', 'batch_size', 'optimizer', 'ml_framework', 'image_loading_lib', 'image_loading_mode', 'loss_fn', 'focal_loss', 'annotation_format', 'dataset_type'
        ], 'title': 'TrainConfig', 'type': 'object'
    }, 'PreProcessConfig': {'properties': {'normalize': {'anyOf': [
                    {'type': 'object'
                    },
                    {'type': 'null'
                    }
                ], 'title': 'Normalize'
            }
        }, 'required': ['normalize'
        ], 'title': 'PreProcessConfig', 'type': 'object'
    }, 'AugmentationConfig': {'$defs': {'AlbumentationsConfig': {'properties': {'GaussNoise': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Gaussnoise'
                    }, 'Blur': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Blur'
                    }, 'MedianBlur': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Medianblur'
                    }, 'ToGray': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Togray'
                    }, 'CLAHE': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Clahe'
                    }, 'RandomBrightnessContrast': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Randombrightnesscontrast'
                    }, 'RandomGamma': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Randomgamma'
                    }, 'ImageCompression': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Imagecompression'
                    }, 'HorizontalFlip': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Horizontalflip'
                    }, 'VerticalFlip': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Verticalflip'
                    }, 'RandomRotate90': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Randomrotate90'
                    }, 'Rotate': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Rotate'
                    }, 'Transpose': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Transpose'
                    }
                }, 'title': 'AlbumentationsConfig', 'type': 'object'
            }, 'YoloTransformationsConfig': {'properties': {'hsv': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': {'h': 0, 's': 0, 'v': 0
                        }, 'metadata': {'description': ''
                        }, 'title': 'Hsv'
                    }, 'degrees': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Degrees'
                    }, 'translate': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Translate'
                    }, 'scale': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Scale'
                    }, 'shear': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Shear'
                    }, 'perspective': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Perspective'
                    }, 'flipud': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Flipud'
                    }, 'fliplr': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Fliplr'
                    }, 'mosaic': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Mosaic'
                    }, 'mixup': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Mixup'
                    }, 'copy_paste': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Copy Paste'
                    }, 'paste_in': {'anyOf': [
                            {'type': 'integer'
                            },
                            {'type': 'number'
                            },
                            {'type': 'object'
                            }
                        ], 'default': 0, 'metadata': {'description': ''
                        }, 'title': 'Paste In'
                    }
                }, 'title': 'YoloTransformationsConfig', 'type': 'object'
            }
        }, 'properties': {'Albumentations': {'allOf': [
                    {'$ref': '#/$defs/AlbumentationsConfig'
                    }
                ], 'default': {}
            }, 'Customs': {'allOf': [
                    {'$ref': '#/$defs/YoloTransformationsConfig'
                    }
                ], 'default': {}
            }
        }, 'title': 'AugmentationConfig', 'type': 'object'
    }, 'DebuggingConfig': {'properties': {'debug_dataset_ratio': {'anyOf': [
                    {'type': 'number'
                    },
                    {'type': 'integer'
                    }
                ], 'title': 'Debug Dataset Ratio'
            }, 'check_dataset': {'default': False, 'title': 'Check Dataset', 'type': 'boolean'
            }
        }, 'required': ['debug_dataset_ratio'
        ], 'title': 'DebuggingConfig', 'type': 'object'
    }, 'ResumeConfig': {'properties': {'resume': {'title': 'Resume', 'type': 'boolean'
            }, 'latest_ckpt': {'anyOf': [
                    {'type': 'string'
                    },
                    {'type': 'null'
                    }
                ], 'default': None, 'title': 'Latest Ckpt'
            }
        }, 'required': ['resume'
        ], 'title': 'ResumeConfig', 'type': 'object'
    }, 'ValConfig': {'properties': {'save_img_ratio': {'anyOf': [
                    {'type': 'number'
                    },
                    {'type': 'integer'
                    }
                ], 'default': 0.5, 'title': 'Save Img Ratio'
            }, 'save_img_freq_epoch': {'default': 9, 'title': 'Save Img Freq Epoch', 'type': 'integer'
            }, 'save_model': {'default': True, 'title': 'Save Model', 'type': 'boolean'
            }, 'save_model_freq_epoch': {'default': 9, 'title': 'Save Model Freq Epoch', 'type': 'integer'
            }, 'save_img_iou': {'title': 'Save Img Iou', 'type': 'number'
            }
        }, 'required': ['save_img_iou'
        ], 'title': 'ValConfig', 'type': 'object'
    }, 'LRConfig': {'properties': {'init_lr': {'title': 'Init Lr', 'type': 'number'
            }, 'end_lr': {'title': 'End Lr', 'type': 'number'
            }, 'scheduler': {'default': 'cosine', 'title': 'Scheduler', 'type': 'string'
            }, 'num_warmup': {'default': 10, 'title': 'Num Warmup', 'type': 'integer'
            }, 'num_hold': {'default': 0, 'title': 'Num Hold', 'type': 'integer'
            }
        }, 'required': ['init_lr', 'end_lr'
        ], 'title': 'LRConfig', 'type': 'object'
    }
}


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
            parsed_prop['type'] = prop['type']

            if 'title' in prop:
                parsed_prop['title'] = prop['title']

            if 'minimum' in prop:
                parsed_prop['minimum'] = prop['minimum']

            if 'maximum' in prop:
                parsed_prop['maximum'] = prop['maximum']

            if 'enum' in prop:
                parsed_prop['enum'] = prop['enum']

            if 'const' in prop:
                parsed_prop['const'] = prop['const']

            if 'default' in prop:
                parsed_prop['default'] = prop['default']

            if 'fronzen' in prop:
                parsed_prop['fronzen'] = prop['fronzen']

            if 'metadata' in prop:
                parsed_prop['metadata'] = prop['metadata']

            # Handle anyOf and allOf
            if 'anyOf' in prop:
                parsed_prop['anyOf'] = [parse_property(p) for p in prop['anyOf']]

            if 'allOf' in prop:
                parsed_prop['allOf'] = [parse_property(p) for p in prop['allOf']]

        return parsed_prop

    for prop_name, prop_details in schema.items():
        result[prop_name] = parse_property(prop_details)

    return result


parsed_schema = parse_json_schema(schema)
print(parsed_schema)