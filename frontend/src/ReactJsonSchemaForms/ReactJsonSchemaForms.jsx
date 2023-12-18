import React, { useEffect, useState } from 'react';
import Form from '@rjsf/mui';
import validator from '@rjsf/validator-ajv8';


const ReactJsonSchemaForms = () => {
  const [schema, setSchema] = useState({});
  const [trainSchema, setTrainSchema] = useState({});
  const [augmentationsSchema, setAugmentationsSchema] = useState({});
  const [networkSchema, setNetworkSchema] = useState({});
  const [config, setConfig] = useState({});

  const handleConfig = ({ formData }) => {
    setConfig(formData);
    console.log('config: ', formData);
  };

  const handleFormSubmit = ({ formData }) => {
    console.log('submit: ', formData);
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
        <h3>Network Configuration</h3>
        <Form
          schema={networkSchema}
          validator={validator}
          onChange={handleConfig}
          onError={log('errors')}
          children={true} // hide the submit button
        />
        <h3>Train Configuration</h3>
        <Form
          schema={trainSchema}
          validator={validator}
          onChange={handleConfig}
          onError={log('errors')}
          children={true} // hide the submit button
        />

        <h3>Augmentations Configuration</h3>
        <Form
          schema={augmentationsSchema}
          validator={validator}
          onChange={handleConfig}
          onError={log('errors')}
          children={true} // hide the submit button
        />
    </div>
  );
};

export default ReactJsonSchemaForms;
