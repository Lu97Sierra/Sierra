const express = require('express');
const router = express.Router();
const mangaController = require('../controllers/mangas');

router.get('/manga',async (req,res)=>{
    try{
        let manga = await mangaController.getMangas()
        res.json(manga);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});
router.post('/manga',async (req,res)=>{
    try{
       let manga = await mangaController.createManga(req.body.name,req.body.price)
        res.json(manga);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});
router.put('/manga',async (req,res)=>{
    try{
        console.log(req.body)
       let manga = await mangaController.modPrice(req.body.mangaId,req.body.newPrice)
        res.json(manga);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});

module.exports = router;