import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
import torch
import numpy as np
import utility
import data
import model
import loss
from option import args
from trainer import Trainer

torch.manual_seed(args.seed)
torch.cuda.manual_seed_all(args.seed)
np.random.seed(args.seed)

def main():
    global model
############ Train ##############
    # args.test_only = False
    # args.save_results = False
    # checkpoint = utility.checkpoint(args)
    # loader = data.Data(args)
    # _model = model.Model(args, checkpoint)
    # _loss = loss.Loss(args, checkpoint) 
    # _lossv = loss.Loss(args, checkpoint, m='validation') 
    # t = Trainer(args, loader, _model, _loss, _lossv, checkpoint)
    # while not t.terminate():
    #     t.train()
    #     t.test()

    # checkpoint.done()


# ############ Test synthetic data ##############
    # print('test synthetic data')
    # args.test_only = True
    # args.save_results = True
    # args.pre_train = '../experiment/alpha6/model/model_best.pt'
    # args.data_range = '1-1600/1-1600'
    # checkpoint = utility.checkpoint(args)
    # loader = data.Data(args)
    # _model = model.Model(args, checkpoint)

    # t = Trainer(args, loader, _model, ckp=checkpoint)
    # t.test()

    # checkpoint.done()

########### Test2 ##############
    print("test field data")
    args.test_only = True
    args.save_dir_suffix = 'field'
    args.data_range = '1-1600/1-3'
    args.dir_lr = '/home/jbgpl/Downloads/SR_denoising/SeismicSuperResolution/data/field'
    args.apply_field_data = True
    args.pre_train = '/home/jbgpl/Downloads/SR_denoising/SeismicSuperResolution/experiment/ESRT_paper/model/model_best.pt'
    checkpoint = utility.checkpoint(args)
    loader = data.Data(args)
    
    _model = model.Model(args, checkpoint)
    #summary = (_model,(128,128))
    t = Trainer(args, loader, _model, ckp=checkpoint)
    t.test()

    checkpoint.done()

if __name__ == '__main__':
    main()



