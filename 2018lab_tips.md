#2018 lab tips
## how to install neuron 7.5 on cluster with python
Follow this paper's appendix  
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2636686/  
Caution! PYTHONPATH might be different. In my case lib64 instead of lib and python 2.6 instead of python

## slack notifier for jobs on cluster
[参考サイト](https://qiita.com/9en/items/23eb3762a9df2c29e812)
```
URL='[please input your URL here]'            
TEXT='process finished'                                                                        
USERNAME='cluster'                                                                             
LINK_NAMES='1'                                                                                 
# post                                                                                         
curl="curl -X POST --data '{\"text\": \"${TEXT}\",\"username\": \"${USERNAME}\" ,\"link_names\"
 : ${LINK_NAMES}}' ${URL}"                                                                     
eval ${curl}                                                                                   
```
