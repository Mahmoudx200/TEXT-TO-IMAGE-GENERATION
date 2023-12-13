# Text To Image Generation Using GAN
Converting text to image, and creating a visualization of specific image content, is a very testing task given the huge semantic gap between the two areas. However, people are dealing with this problem intelligently. Make use of various elements to create a powerful early frame around semantics, surfaces, shadows, shapes, and layouts. Looking at content photography, I quickly imagine a general visual impression that uses this earlier, and in light of this, I paint an image by constantly adding an increasing number of fine details. Merging cool pictures from text images is a difficult problem with PC vision and has many plausible applications. The tests created with the content-to-image approach can generally reflect the significance of specific images, but ignore the containment of essential fine details and bits of stunning elements. In this project, Stacked Generative Adversarial Networks (AttnGAN) was proposed to create plausible 256 x 256 photographs adapted to content imagery. It is a project to graphically convert text using machine learning and deep learning using some of the research that some programmers have previously done in the use of Generative Adversarial Networks (GANs).

![image](https://github.com/Mahmoudx200/Text-To-Image-Generation/assets/119981830/9deee611-2ce3-4f33-8fd4-6fd95de1b56f)


******************************************************************************************
To run the program you must steps the following:

In addition, please add the project folder to PYTHONPATH and `pip install` the following packages (or go `pip install -r requirements.txt`):

**Dependencies:**
1. python 3.7+ 
2. Pytorch 1.0+
3. python-dateutil
4. easydict
5. pandas
6. torchfile
7. nltk
8. scikit-image
9. pyyaml
10. tqdm
11. pytorch-fid
12. lpips
13. transformers
14. gan-lab

******************************************************************************************

**Dataset**
1. Download preprocessed metadata from taoxugit for [birds](https://drive.google.com/open?id=1O_LtUP9sch09QH3s_EBAgLEctBQ5JBSJ) [coco](https://drive.google.com/open?id=1rSnbIGNDGZeHlsUlLdahj0RJ9oo6lgH9) and save them to `data/
2. Unzip `data/birds/text.zip` and/or `data/coco/train2014-text.zip` & `data/coco/val2014-text.zip`
3. Download the [birds](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) image data. Extract them to `data/birds/`
4. Download [coco](http://cocodataset.org/#download) dataset and extract the images to `data/coco/`

******************************************************************************************

**Pretrained Model**
- [DAMSM for bird](https://drive.google.com/open?id=1GNUKjVeyWYBJ8hEU-yrfYQpDOkxEyP3V). Download and save it to `DAMSMencoders/`
- [DAMSM for coco](https://drive.google.com/open?id=1zIrXCE9F6yfbEJIbNP5-YrEe2pZcPSGJ). Download and save it to `DAMSMencoders/`
- [Style-AttnGAN for bird](https://drive.google.com/file/d/11Fo003VQJbXK9OBT18PESlP6wqtbaQAo/view?usp=sharing). Download and save it to `models/`
- [Original AttnGAN for bird](https://drive.google.com/open?id=1lqNG75suOuR_8gjoEPYNp8VyT_ufPPig). Download and save it to `models/`
- [Original AttnGAN for coco](https://drive.google.com/open?id=1i9Xkg9nU74RAvkcqKE-rJYhjvzKAMnCi). Download and save it to `models/`
- [AttnDCGAN for bird](https://drive.google.com/open?id=19TG0JUoXurxsmZLaJ82Yo6O0UJ6aDBpg). Download and save it to `models/`

******************************************************************************************

**Training**
- Pre-train DAMSM models:
  - For bird dataset: `python train.py --cfg cfg/DAMSM/bird.yml --gpu 0`
  - For coco dataset: `python train.py --cfg cfg/DAMSM/coco.yml --gpu 0`
 
- Train Style-AttnGAN models:
  - For bird dataset: `python main.py --cfg cfg/bird_attn2_style.yml --gpu 0`
  - For coco dataset: `python main.py --cfg cfg/coco_attn2_style.yml --gpu 0`

- Train original AttnGAN models:
  - For bird dataset: `python main.py --cfg cfg/bird_attn2.yml --gpu 0`
  - For coco dataset: `python main.py --cfg cfg/coco_attn2.yml --gpu 0`

******************************************************************************************

  **Sampling**
- Run `python main.py --cfg cfg/eval_bird.yml --gpu 0` to generate examples from captions in files listed in "./data/birds/example_filenames.txt". Results are saved in `models/`. 
- Change the `eval_*.yml` files to generate images from other pre-trained models. 
- Input your own sentence in "./data/birds/example_captions.txt " if you wannt to generate images from customized sentences.
