"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
const express_1 = __importDefault(require("express"));
const product_router_1 = __importDefault(require("./routes/product.router"));
const app = (0, express_1.default)();
app.use(express_1.default.json());
app.use('/products', product_router_1.default);
module.exports = app;
