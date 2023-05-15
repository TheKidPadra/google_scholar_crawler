import pickle

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Recommender+system&btnG='

    #p_key = ['regression', 'supervise', 'unsupervised', 'speech',
    #         'vision', 'noise recognition', 'cost',
    #         'sound', 'nlp' , 'python']
    #n_key = ['imagery', 'visual', 'segmentation', 'reflect', 'quantum',
    #         'photon']

    p_key = ['sentiment analysis', 'emotion detection', 'recommendation', 'recommender system',
             'text', 'emotion identificayion']
    n_key = ['speech', 'voice', 'persian', 'farsi', 'signal']


    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url, p_key, n_key, page=20)

    results = myCrawler.crawl()

    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
