// Your React component file

import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/styles';
import './styles.css';

const useStyles = makeStyles({
  device_ids: {
    marginLeft: 10,
    marginRight: 10,
    padding: 10,
    width: 400,
  },
});

function TrainFieldTemplate(props) {
  const classes = useStyles();
  return (
    <div>
      <h4 className='title'>{props.title}</h4>
      <div className='description'>
        {props.description}
      </div>
      <Grid container={true} spacing={1} className='container'>
        {props.properties.map((element, index) => {
          if (element.content.key === 'device_ids'){
            return (
              <div className={classes.device_ids}>{element.content}</div>
            )
          }
          else {
            return (
              <div className='elements'>{element.content}</div>
            )
          }
        })}
      </Grid>
    </div>
  );
}

export default TrainFieldTemplate;
