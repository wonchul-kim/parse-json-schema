import React, { useEffect, useState } from 'react';
import Form from '@rjsf/mui';
import validator from '@rjsf/validator-ajv8';

import DataFieldTemplate from './Templates/DataFieldTemplate';
import RoiFieldTemplate from './Templates/RoiFieldTemplate';
import PatchFieldTemplate from './Templates/PatchFieldTemplate';
import PreprocessFieldTemplate from './Templates/PreProcessFieldTemplate copy';
import ModelFieldTemplate from './Templates/ModelFieldTemplate';
import TrainFieldTemplate from './Templates/TrainFieldTemplate';
import ValFieldTemplate from './Templates/ValFieldTemplate';
import AugmentationsFieldTemplate from './Templates/AugmentationsFieldTemplate';

const ReactJsonSchemaForms = () => {
  const [schema, setSchema] = useState({});
  const [dataSchema, setDataSchema] = useState({});
  const [patchSchema, setPatchSchema] = useState({});
  const [roiSchema, setRoiSchema] = useState({});
  const [preprocessSchema, setPreprocessSchema] = useState({});
  const [trainSchema, setTrainSchema] = useState({});
  const [valSchema, setValSchema] = useState({});
  const [augmentationsSchema, setAugmentationsSchema] = useState({});
  const [modelSchema, setModelSchema] = useState({});
  const [config, setConfig] = useState({});
  const [trainConfig, setTrainConfig] = useState({});
  const [modelConfig, setModelConfig] = useState({});
  const [augmentationsConfig, setAugmentationsConfig] = useState({});


  // const handleConfigChanges = ({ key, formData }) => {
  //   setConfig({...prevformData => prevformData, [key]: formData});
  //   console.log('config: ', formData);
  // };
  const handleConfigChanges = (type) => ({ formData }) => {
    setConfig((prevDynamicState) => ({
      ...prevDynamicState,
      [type]: { ...prevDynamicState[type], ...formData },
    }));
  };
  
  const handleJsonSchema = (data) => {
    setSchema(data);
    setDataSchema(data['DataConfig']);
    setPatchSchema(data['PatchConfig']);
    setRoiSchema(data['RoiConfig']);
    setPreprocessSchema(data['PreProcessConfig']);
    setTrainSchema(data['TrainConfig']);
    setValSchema(data['ValConfig']);
    // setAugmentationsSchema(data['AugmentationConfig']);
    // setModelSchema(data['ModelConfig']);
  };

  useEffect(() => {
    fetch('http://localhost:8000/schema/')
      .then((response) => response.json())
      .then((data) => {
        handleJsonSchema(data);
        console.log('Fetched schema:', data);
      })
      .catch((error) => console.error('Error fetching schema:', error));
  }, []);

  const log = (type) => console.log.bind(console, type);

  return (
    <div className="form-container">
      <h1>React Json Schema Form</h1>
        <Form
          schema={dataSchema}
          validator={validator}
          onChange={handleConfigChanges('data')}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{
            "ui:ObjectFieldTemplate": DataFieldTemplate
          }}        
        />
        <Form
          schema={patchSchema}
          validator={validator}
          onChange={handleConfigChanges('patch')}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{
            "ui:ObjectFieldTemplate": PatchFieldTemplate
          }}        
        />
        <Form
          schema={roiSchema}
          validator={validator}
          onChange={handleConfigChanges('roi')}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{
            "ui:ObjectFieldTemplate": RoiFieldTemplate
          }}        
        />
        <Form
          schema={preprocessSchema}
          validator={validator}
          onChange={handleConfigChanges('preprocess')}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{
            "ui:ObjectFieldTemplate": PreprocessFieldTemplate
          }}        
        />
        
        <Form
          schema={modelSchema}
          validator={validator}
          onChange={handleConfigChanges('model')}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{ "ui:ObjectFieldTemplate": ModelFieldTemplate }}
        
        />

        <Form
          schema={trainSchema}
          validator={validator}
          onChange={handleConfigChanges('train')}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{
            "ui:ObjectFieldTemplate": TrainFieldTemplate
          }}        
        />

        <Form
          schema={valSchema}
          validator={validator}
          onChange={handleConfigChanges('val')}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{
            "ui:ObjectFieldTemplate": ValFieldTemplate
          }}        
        />

        <Form
          schema={augmentationsSchema}
          validator={validator}
          onChange={handleConfigChanges('augmentations')}
          onError={log('errors')}
          children={true} // hide the submit button
          // uiSchema={{"ui:ObjectFieldTemplate": AugmentationsFieldTemplate}}
        />
    </div>
  );
};

export default ReactJsonSchemaForms;
