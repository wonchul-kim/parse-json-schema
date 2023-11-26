import React, { useEffect, useState } from 'react';
import Form from '@rjsf/material-ui';
import { ThemeProvider} from '@mui/material/styles';
import { Theme } from '@rjsf/material-ui';
import validator from '@rjsf/validator-ajv8';



const ParameterSettingsPage = () => {
  const [parameterSchema, setParameterSchema] = useState({});

  useEffect(() => {
    fetch('http://localhost:8000/schema/')
      .then(response => response.json())
      .then(data => {
        setParameterSchema(data);
        console.log('Fetched schema:', data);
      })
      .catch(error => console.error('Error fetching schema:', error));
  }, []);

  const log = (type) => console.log.bind(console, type);

  return (
      <Form 
        schema={parameterSchema}
        validator={validator}
        uiSchema={uiSchema}
        // onChange={log('changed')}
        // onSubmit={log('submitted')}
        // onError={log('errors')}
      />
  );
};

export default ParameterSettingsPage;
