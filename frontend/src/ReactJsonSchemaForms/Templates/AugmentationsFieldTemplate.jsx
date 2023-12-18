// Your React component file

import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/styles';
import './styles.css';

const useStyles = makeStyles({
  hsv: {

  },

});

function AugmentationsFieldTemplate(props) {
  const classes = useStyles();
  return (
    <div>
      <h4 className='title'>{props.title}</h4>
      <div className='description'>
        {props.description}
      </div>
      <Grid container={true} spacing={1} className='container'>
        {props.properties.map((element, index) => {
          console.log(">>>> ", element, element.content)
          return (
            <div className='elements'>{element.content}</div>
          )
        })}
      </Grid>
    </div>
  );
}

export default AugmentationsFieldTemplate;
