import React, { useEffect, useState } from 'react';
import Form from '@rjsf/mui';
import validator from '@rjsf/validator-ajv8';

import TrainFieldTemplate from './Templates/TrainFieldTemplate';
import ModelFieldTemplate from './Templates/ModelFieldTemplate';
import AugmentationsFieldTemplate from './Templates/AugmentationsFieldTemplate';

const ReactJsonSchemaForms = () => {
  const [schema, setSchema] = useState({});
  const [trainSchema, setTrainSchema] = useState({});
  const [augmentationsSchema, setAugmentationsSchema] = useState({});
  const [networkSchema, setNetworkSchema] = useState({});
  const [config, setConfig] = useState({});
  const [trainConfig, setTrainConfig] = useState({});
  const [modelConfig, setModelConfig] = useState({});
  const [augmentationsConfig, setAugmentationsConfig] = useState({});

  const handleConfigChanges = ({ formData }) => {
    setConfig(formData);
    console.log('config: ', formData);
  };

  const handleJsonSchema = (data) => {
    setSchema(data);
    setTrainSchema(data['TrainConfig']);
    setAugmentationsSchema(data['AugmentationConfig']);
    setNetworkSchema(data['NetworkConfig']);
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
          schema={networkSchema}
          validator={validator}
          onChange={handleConfigChanges}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{ "ui:ObjectFieldTemplate": ModelFieldTemplate }}
        
        />

        <Form
          schema={trainSchema}
          validator={validator}
          onChange={handleConfigChanges}
          onError={log('errors')}
          children={true} // hide the submit button
          uiSchema={{
            "ui:ObjectFieldTemplate": TrainFieldTemplate
          }}        
        />

        <Form
          schema={augmentationsSchema}
          validator={validator}
          onChange={handleConfigChanges}
          onError={log('errors')}
          children={true} // hide the submit button
          // uiSchema={{"ui:ObjectFieldTemplate": AugmentationsFieldTemplate}}
        />
    </div>
  );
};

export default ReactJsonSchemaForms;
