lane_cfg = {
    "src_shape":(960, 540),
    "dst_shape":(960, 540),
    "zero_pads":[0,0],
    "mean":[0.5, 0.5, 0.5],
    "std":[0.5, 0.5, 0.5],
    'test_images':3055,
    "train_images":19222,
    "lr":0.0002,
    #"lr":0.001,
    "batch_size": 8,
    "snapshot": 1,
    "num_epochs": 20,
    "begin_epoch":1,
    "num_gpus":4,
    "lovasz_loss":True,
    "lovasz_weight":0.2,

    #hrnet
    #"model":"hrnet",
    #"to_rgb":False,
    #"savd_dir":"/data_bk/ai_lane/saved_model/hrnet_320_180/",
    #"pretrained":"/data_bk/ai_lane/pretrained_model/hrnet_w64_bn_imagenet",
    #"pretrained":"/data_bk/ai_lane/saved_model/hrnet_320_180/2/",
    #"result_dir":"/data_bk/ai_lane/res_hrnet_320_180/",
    #"infer_model":"/data_bk/ai_lane/saved_model/hrnet_320_180/10/",

    #deeplab
    #"model":"deeplab",
    #"to_rgb":True,
    #"savd_dir":"/data_bk/ai_lane/saved_model/deeplab3pro_resnet50/",
    #"pretrained":"/data_bk/ai_lane/pretrained_model/ResNet50_vd_ssld_pretrained",
    #"infer_model":"/data_bk/ai_lane/saved_model/deeplab3pro_resnet50/20/",
    #"result_dir":"/data_bk/ai_lane/res_deeplab_medium/",

    #ocrnet
    "model": "ocrnet",
    "to_rgb":True,
    "savd_dir": "saved_model/ocrnet_960_540/",
    "pretrained": "pretrained_model/ocnet_w18_bn_cityscapes/",
    "infer_model": "saved_model/ocrnet_960_540_epoch_14/",
    "result_dir": "result/ocrnet_960_540/",

    #数据集
    "data_dir":"dataset/",
    "train_list":"dataset/trainval_list_balance_v10.txt",
    "val_list":"dataset/val_list_C.txt",
    "test_list":"dataset/test_list.txt",
}

if __name__ == "__main__":
    print("Hello")
