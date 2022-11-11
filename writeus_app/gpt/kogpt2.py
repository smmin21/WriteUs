# -*- coding: utf-8 -*-
"""kogpt2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t_jqwKZVif1wexjBGLNrIFu9jj049ENt
"""

class kogpt2:
    def __init__(self):
        # !pip install -q torch~=1.9.0 transformers~=4.12.0

        import torch
        from transformers import GPT2LMHeadModel
        from transformers import PreTrainedTokenizerFast
        
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
        bos_token='</s>', eos_token='</s>', unk_token='<unk>',
        pad_token='<pad>', mask_token='<mask>')

        self.model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')

    def text_generator(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors='pt')
        gen_ids = self.model.generate(input_ids,
                           max_length=64,
                           repetition_penalty=2.0,
                           pad_token_id=self.tokenizer.pad_token_id,
                           eos_token_id=self.tokenizer.eos_token_id,
                           bos_token_id=self.tokenizer.bos_token_id,
                           use_cache=True)
        generated = self.tokenizer.decode(gen_ids[0])
        gen_id = generated.split("\n")
        if '</d>' in gen_id[0]:
            generated = gen_id[0].split("</d>")
            generated = generated[1] 
        else:
            if '</d>' in gen_id[1]:
                generated = gen_id[1].split("</d>")
                generated = generated[1]
            else:
                generated = generated[1]
        return generated