import connection from '../models/connection';
import ProductModel from '../models/product.model';
import Product from '../interface/product.interface';

class ProductService {
    public model: ProductModel;

    constructor() {
      this.model = new ProductModel(connection);
    };

    public async getAll(): Promise<Product[]> {
      const products = await this.model.getAll();
      return products;
    };
};

export default ProductService;