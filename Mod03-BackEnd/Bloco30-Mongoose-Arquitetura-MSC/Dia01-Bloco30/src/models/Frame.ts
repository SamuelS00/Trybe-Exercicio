import { model as mongooseCreateModel, Schema } from 'mongoose';
import IFrame from '../interfaces/Frame';
import MongoModel from './MongoModel';

const frameMongooseSchema = new Schema<IFrame>({
  material: String,
  color: String });

class Frame extends MongoModel<IFrame> {
  constructor(model = mongooseCreateModel('Frame', frameMongooseSchema)) {
    super(model);
  }
  // 'Frame' model que referencia o documento
}

export default Frame;