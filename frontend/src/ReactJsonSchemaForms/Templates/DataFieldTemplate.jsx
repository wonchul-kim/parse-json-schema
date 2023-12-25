// Your React component file

import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/styles';
import './styles.css';

const useStyles = makeStyles({
  directory: {
    marginLeft: 10,
    marginRight: 10,
    padding: 10,
    width: 900,
  },
});

function DataFieldTemplate(props) {
  const classes = useStyles();
  return (
    <div>
      <h4 className='title'>{props.title}</h4>
      <div className='description'>
        {props.description}
      </div>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
          if (['input_dir', 'output_dir', 'classes'].includes(element.content.key)){
            return (
              <div className={classes.directory}>{element.content}</div>
            )
          }
        })}
      </Grid>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
          if (['image_exts'].includes(element.content.key)){
            return (
              <div className={classes.directory}>{element.content}</div>
            )
          }
        })}
      </Grid>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
          if (!['input_dir', 'output_dir', 'classes', 'image_exts'].includes(element.content.key)){
            return (
              <div className='elements'>{element.content}</div>
            )
          }
        })}
      </Grid>
    </div>
  );
}

export default DataFieldTemplate;
