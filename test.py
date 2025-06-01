import torch
import torchvision
#测试模型权重是否完整
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.cuda.is_available())

model = torch.load('/root/siton-tmp/TCM/ocrclip/output/AlphaTCM_IC15_20_epoch200_withNor/Longclip77_18/clip_db_r50_fpnc_prompt_gen_vis_1200e_ft_gen_ic15_adam_taiji_0411_233040/best_0_icdar2015_test_hmean-iou_hmean_epoch_170.pth')
print(model)

# zero_alpha = torch.zeros(6,3,64,64).cuda()
# print(zero_alpha)

