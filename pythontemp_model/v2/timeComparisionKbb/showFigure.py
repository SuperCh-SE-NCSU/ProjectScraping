import matplotlib.pyplot as plt
import numpy as np  
def showdata():  
    n_groups = 4 
    means_1 =(49.5111749172, 36.754598856, 91.7958290577, 102.909796953)  
    means_2 = (11.565237999, 7.44670701027, 15.6577756405, 15.3676428795)
    #means_3 =(9.05211806297,7.70969510078,19.7910189629,11.4580149651)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.2  
   
    opacity = 0.8  
    rects1 = plt.bar(0.8+index, means_1, bar_width,alpha=opacity, color='b',label='Recursive')  
    rects2 = plt.bar(0.8+index + bar_width, means_2, bar_width,alpha=opacity,color='r',label='Based on parameter')  
    #rects3 = plt.bar(0.8+index +2*bar_width, means_3,bar_width,alpha=opacity,color='g',label='Scrapy')
    plt.xlabel('Group')  
    plt.ylabel('Time(s)')  
    plt.title('Time to crawl craigslist using three methods')  
    plt.xticks(0.8+index + bar_width, ('Camry', 'Corolla','Accord','Civic'))  
    plt.xlim(0,5)
    plt.ylim(0,120)  
    plt.legend()  
   
    plt.tight_layout()  
    plt.show()

showdata()
