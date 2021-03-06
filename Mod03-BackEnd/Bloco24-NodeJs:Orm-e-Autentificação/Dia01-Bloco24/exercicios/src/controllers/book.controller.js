const bookController = require('../services/book.service');

const getAllBooks = async (req, res, _next) => {
  const books = await bookController.getAllBooks();
  
  return res.status(200).json(books);
};

const getByIdBook = async (req, res, _next) => {
  const { id } = req.params;
  const book = await bookController.getByIdBook(id);

  return res.status(200).json(book)
};

const getByAuthor = async (req, res, _next) => {
  const { author } = req.query;
  const books = await bookController.getByAuthor(author);
  
  return res.status(200).json(books);
};

const create = async (req, res, _next) => {
  const { title, author, pageQuantity, publisher } = req.body;
  const newBook = await bookController.create(title, author, pageQuantity, publisher);

  return res.status(201).json(newBook);
};

const update = async (req, res, _next) => {
  const { id } = req.params;
  const { title, author, pageQuantity, publisher} = req.body;
  const response = await bookController.update(id, title, author, pageQuantity, publisher);

  return res.status(201).json(response.message);
};

const destroy = async (req, res, _next) => {
  const { id } = req.params;
  const response = await bookController.destroy(id);

  return res.status(200).json(response.message);
};

module.exports = {
  getAllBooks,
  getByIdBook,
  create,
  update,
  destroy,
  getByAuthor 
};