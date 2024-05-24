const express = require('express');
const router = express.Router();
const userController = require('../controllers/users');

router.get('/user',async (req,res)=>{
    try{
        let clients = await userController.getUsers()
        res.json(clients);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});
router.post('/user',async (req,res)=>{
    try{
       let client = await userController.createUser(req.body.email,req.body.password)
        res.json(client);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});
router.put('/user',async (req,res)=>{
    try{
        console.log(req.body)
       let client = await userController.modPassword(req.body.id,req.body.password)
        res.json(client);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});

module.exports = router;