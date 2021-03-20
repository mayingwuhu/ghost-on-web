#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# 僵尸虾模拟器beta 0.0.1

# In[1]:



get_ipython().system(' pip install xlrd')
get_ipython().system(' pip install paddlehub==1.8.0')
get_ipython().system(' pip install paddle-ernie==0.0.4.dev1')


# In[2]:


import pandas as pd
#xlsx数据格式：标签/内容
df = pd.read_excel("test1.xlsx")
Keys = df["tag"].values
Txts = df["content"].values

with open("format_data2.txt", "w") as f:
    for i, k in enumerate(Keys):
        t = Txts[i]
        f.write("{}\t{}\t{}\n".format(i, k, t))


# In[3]:


import paddlehub as hub
get_ipython().system('hub install Versailles')

module = hub.Module(name="ernie_gen")

result = module.finetune(
    train_path='format_data2.txt',
    save_dir="Versailles_param",
    max_steps=1200,
    noise_prob=0.1,
    save_interval=400,
    max_encode_len=60,
    max_decode_len=60
)

# 将训练参数打包为hub model
module.export(params_path=result['last_save_path'], module_name="Versailles", author="lyp")


# ## 3. 运行预测

# In[4]:


import paddlehub as hub

module = hub.Module(directory="/home/aistudio/Versailles/")


# In[13]:



test_texts = ["肖战"]
results = module.generate(texts=test_texts, use_gpu=True, beam_width=30)
for result in results[0]:
    print(result)


# 可以看到数据集太少，出现了明显的过拟合现象，可以多搜集一些。
