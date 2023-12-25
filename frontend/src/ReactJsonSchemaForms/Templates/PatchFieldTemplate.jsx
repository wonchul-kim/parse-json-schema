// Your React component file

import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/styles';
import './styles.css';

const useStyles = makeStyles({
  checkboxes: {
    marginLeft: 10,
    marginRight: 10,
    padding: 10,
    width: 400,
  },
});

const list_1 = ['use_patch', 'centric', 'sliding'];
const list_2 = ['width', 'height', 'overlap_ratio', 'num_involved_pixels', 'include_point_positive'];
const list_3 = ['translate', 'translate_range_width', 'translate_range_height'];
const list_4 = ['use_patch', 'centric', 'sliding'];

function PatchFieldTemplate(props) {
  const classes = useStyles();
  return (
    <div>
      <h4 className='title'>{props.title}</h4>
      <div className='description'>
        {props.description}
      </div>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
          if (list_1.includes(element.content.key)){
            return (
              <div className='elements'>{element.content}</div>
            )
          }
        })}
      </Grid>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
          if (list_2.includes(element.content.key)){
            return (
              <div className='elements'>{element.content}</div>
            )
          }
        })}
      </Grid>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
          if (list_3.includes(element.content.key)){
            return (
              <div className='elements'>{element.content}</div>
            )
          }
        })}
      </Grid>
      <Grid container={true} spacing={1} className='container' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {props.properties.map((element, index) => {
          if (!(list_1 + list_2 + list_3).includes(element.content.key)){
            return (
              <div className='elements'>{element.content}</div>
            )
          }
        })}
      </Grid>
    </div>
  );
}

export default PatchFieldTemplate;
