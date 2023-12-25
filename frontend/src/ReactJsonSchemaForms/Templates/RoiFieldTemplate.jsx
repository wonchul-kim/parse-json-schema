// Your React component file

import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/styles';
import './styles.css';

const useStyles = makeStyles({
  roi: {
    marginLeft: 10,
    marginRight: 10,
    padding: 10,
    width: 250,
  }, 
});

function RoiFieldTemplate(props) {
  const classes = useStyles();
  return (
    <div>
      <h4 className='title'>{props.title}</h4>
      <div className='description'>
        {props.description}
      </div>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
        if (!['top_left_x', 'top_left_y', 'width', 'height'].includes(element.content.key)) {
            return (
              <div className='elements'>{element.content}</div>
            )
          }
        })}
      </Grid>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
        if (['top_left_x', 'top_left_y', 'width', 'height'].includes(element.content.key)) {
          return (
              <div className={classes.roi}>{element.content}</div>
            )
          }
        })}
      </Grid>
    </div>
  );
}

export default RoiFieldTemplate;
