var express = require('express');
var router = express.Router();
var nodemailer= require('nodemailer');
const novedadesModel = require('../models/novedadesModel');

router.get('/', function(req, res, next) {
  res.render('contacto', { title: 'Express' });
});

router.post('/', async (req, res, next)=>{
  console.log(req.body);
  var nombre= req.body.nombre;
  var email=req.body.email;
  var telefono=req.body.telefono;
  var mensaje=req.body.comentario;

  var obj={
    to:'eskilax1000@gmail.com',
    subject:'Contacto desde la web',
    html: nombre + ", Se contactó y quiere mas información a este correo: "+ email +".<br> Además, comentó: "+ mensaje + ". <br> Su teléfono es "+ telefono
  }
  var transport = nodemailer.createTransport({
     host:process.env.SMTP_HOST,
     port:process.env.SMTP_PORT,
     auth:{
       user:process.env.SMTP_USER,
       pass:process.env.SMTP_PASS
     }
   });
  var info = await transport.sendMail(obj);
  res.render('contacto', {
    message:'Mensaje enviado correctamente'
  });

  try{
    if(req.body.nombre != "" && req.body.email != "" && req.body.telefono != "" && req.body.comentario !=""){
      await novedadesModel.insertContactos(req.body);
      res.redirect('contacto');
    }else{
      res.render('contacto',{
        layout:'layout',
        error:true,
        mensaje:'Todos los campos son requeridos'
      });
    }
  
  }catch (error){
    console.log(error)
    res.render('contacto',{
      layout:'layout',
      error:true,
      mensaje:'No se cargo la solicitud'
    });
  };
  ;

});


module.exports = router;

