const express = require('express');
const router = express.Router();
const libraryController = require('../controllers/library');

router.get('/library',async (req,res)=>{
    try{
        let library = await libraryController.getLibrarys()
        res.json(library);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});
router.post('/library', async (req, res) => {
    try {
        // Verificación de que `mangas` es un array de números
        if (!Array.isArray(req.body.mangas)) {
            throw new Error("`mangas` debe ser un array de números");
        }
        
        let library = await libraryController.createLibrary(req.body.name, req.body.mangas);
        res.json(library);
    } catch (ex) {
        res.status(500).json({ message: ex.message });
    }
});
router.put('/library',async (req,res)=>{
    try{
        console.log(req.body)
       let library = await libraryController.modName(req.body.LibraryId,req.body.newName)
        res.json(library);
    }catch(ex){
        res.status(500).json({ message: ex.message });
    }
});

module.exports = router;