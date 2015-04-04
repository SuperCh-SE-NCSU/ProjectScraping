import matplotlib.pyplot as plt
import numpy as np  
def showdata():  
    n_groups = 4 
    means_1 =(11.352260112762451, 7.856437921524048, 43.17771887779236, 8.285339117050171)  
    means_2 = (16.72474503517151, 14.028115034103394, 53.29979920387268, 18.483553171157837)
    means_3 =(9.05211806297,7.70969510078,19.7910189629,11.4580149651)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.2  
   
    opacity = 0.8  
    rects1 = plt.bar(0.8+index, means_1, bar_width,alpha=opacity, color='b',label='Regular Regression')  
    rects2 = plt.bar(0.8+index + bar_width, means_2, bar_width,alpha=opacity,color='r',label='BeautifulSoup')  
    rects3 = plt.bar(0.8+index +2*bar_width, means_3,bar_width,alpha=opacity,color='g',label='Scrapy')
    plt.xlabel('Group')  
    plt.ylabel('Time(s)')  
    plt.title('Time to crawl craigslist using three methods')  
    plt.xticks(0.8+index + bar_width, ('Camry', 'Corolla','Accord','Civic'))  
    plt.xlim(0,5)
    plt.ylim(0,60)  
    plt.legend()  
   
    plt.tight_layout()  
    plt.show()

showdata()
