import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

function controllerRouting(app) {
  const router = express.Router();
  app.use('/', router);

  router.get('/', (req, res) => {
    AppController.getHomepage(req, res);
  });

  router.get('/students', (req, res) => {
    StudentsController.getAllStudents(req, res, process.argv[2]);
  });

  router.get('/students/:major', (req, res) => {
    StudentsController.getAllStudentsByMajor(req, res, process.argv[2]);
  });
}

export default controllerRouting;
