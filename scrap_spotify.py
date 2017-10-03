
# importing modules
import requests,sys
from bs4 import BeautifulSoup as bs
import pandas as pd
import itunes,re

class spotify:
    def spotify_scraper(self, url):
        position=[]
        track=[]
        artist=[]
        streams=[]

        session = requests.Session()
        response = session.get(url)
        soup = bs(response.content, 'html.parser')

        for data in soup.find_all('td',{"class":"chart-table-position"}):
                position.append(data.text)
        for data in soup.find_all('td',{"class":"chart-table-track"}):
            for inner in data.find_all('strong'):
                track.append(inner.text)
            for inner in data.find_all('span'):
                artist.append(inner.text)
        for data in soup.find_all('td', {"class": "chart-table-streams"}):
            streams.append(data.text)
        # print(position)
        # print(track)
        # print(artist)
        return position,track,artist,streams

    def itunes_scraper(self,track,artist):
        x=2 # To track the length of label
        label=[]
        itunes_url=[]
        problematic_indices=[]
        for i,inside in enumerate(track):
            # print("Track:")
            # print(i,artist[i].replace("by ","")+' '+track[i])
#            print(i, artist[i].replace("by ", "") + ' ' + track[i].encode('ascii', 'ignore'))

#            sys.exit()
            # Temp code
            # data = itunes.search("Me Rehso danny ocean")
            # print(data)
            # for items in data:
            #     print(items.get_url())
            # sys.exit()

            try: # This sometimes throw Itunes error if somehting goes wrong
                data=itunes.search(artist[i].replace("by ","")+' '+track[i].encode('ascii', 'ignore'))
            except:
                print("Itunes api problem")
                problematic_indices.append(i)
                ### Two blank strings are added to list label if sth goes wrong with the artist+ track combined string through itunes api
                label.append('')
                label.append('')
                itunes_url.append('')
                continue
            urls = []
            for items in data:
                urls.append(items.get_url())
            session = requests.Session()
            if not(len(urls)==0):
                # print("Url:")
                # print(urls[0]+"\n")
                itunes_url.append(urls[0])
                response = session.get(urls[0])
                soup = bs(response.content, 'html.parser')
                for data in soup.find_all("p",{"class":"t-sosumi"}):
#                     print(str(data.text.encode(sys.stdout.encoding, errors='replace'))[str(data.text.encode(sys.stdout.encoding, errors='replace')).find("?")+7:len(str(data.text.encode(sys.stdout.encoding, errors='replace')))])
# #Can place a "Song text check here"
#                     label.append(str(data.text.encode(sys.stdout.encoding, errors='replace'))[
#                       str(data.text.encode(sys.stdout.encoding, errors='replace')).find("?") + 7:len(
#                           str(data.text.encode(sys.stdout.encoding, errors='replace')))])

                    # print(str(data.text.encode(sys.stdout.encoding, errors='replace')))
                    # print(str(data.text.encode(sys.stdout.encoding, errors='replace'))[str(data.text.encode(sys.stdout.encoding, errors='replace')).find("2017")+4:len(str(data.text.encode(sys.stdout.encoding, errors='replace')))])

                    label.append(str(data.text.encode(sys.stdout.encoding, errors='replace'))[
                      str(data.text.encode(sys.stdout.encoding, errors='replace')).find("2017") + 4:len(
                          str(data.text.encode(sys.stdout.encoding, errors='replace')))])
            else:
                print("--------------------not found case------------------")
                label.append('')
                label.append('')
                itunes_url.append('')
                problematic_indices.append(i)
            if not(len(label)==x):
                print("The length of label list and iteration is not matching,label list missed two elements that was supposed to be append")
                print(x,len(label),label)
                print("The iteration is "+str(i))
                print("The track being searched is "+artist[i].replace("by ","")+' '+track[i].encode('ascii', 'ignore'),"problematic_indices",problematic_indices
                      ,"urls",urls)
                #sys.exit()
            print("\n"+" length of label list ") #should be multiple of 2 and equal to twice the current index in the iteration
            print(x, len(label))
            x = x + 2
        return label,itunes_url,problematic_indices


if __name__=="__main__":
    x=2
    label2=[]
    label3=[]
    obj=spotify()
    position, track, artist,streams=obj.spotify_scraper("https://spotifycharts.com/regional/global/weekly/2017-09-15--2017-09-22")
#    index=[range(len(position))]
    excel1=pd.DataFrame({'Rank':position,'Track':track,'Artist':artist,"Number of Streams":streams})
    for i,strings in enumerate(track):
        track[i]=strings.encode('ascii', 'ignore')
#    excel1.to_csv("streaming_music_industry_trakcer_without_labels.csv",encoding='utf-8',index='False')
    label,itunes_url,problematic_indices=obj.itunes_scraper(track,artist)
    for i,lab in enumerate(label):
        if (i+1)%2==0:
            label3.append(lab)
        if not(re.search("Song",lab)):
            label2.append(lab)
    print("label",len(label),"label2",len(label2),"label3",len(label3),"url",len(itunes_url),"problematic_indices",problematic_indices)
    # position=position
    # track=track
    # artist=artist
    # streams=streams
#    print(label2[8, 55, 58, 83, 84, 98, 158, 182])
 #   print(label2[22])
    excelx=pd.DataFrame({'Rank':position,'Track':track,'Artist':artist,"Number of Streams":streams,"Itunes_url":itunes_url})
    excelx.to_csv("x.csv", index=False)

    excel2=pd.DataFrame({'Rank':position,'Track':track,'Artist':artist,"Number of Streams":streams,"Label":label3,"Itunes_url":itunes_url})
    print(excel2)

    excel2['Label']=excel2['Label'].str.decode('iso-8859-1').str.encode('utf-8')
    # def changeencode(data, cols):
    #     for col in cols:
    #         data[col] = data[col].str.decode('iso-8859-1').str.encode('utf-8')
    #     return data

    # for i,strings in enumerate(label3):
    #     label3[i]=strings.str.decode('iso-8859-1').str.encode('utf-8')
    # for i,strings in enumerate(itunes_url):
    #     itunes_url[i]=strings.str.decode('iso-8859-1').str.encode('utf-8')


#    excel2=pd.DataFrame({'Rank':position,'Track':track,'Artist':artist,"Number of Streams":streams,"Label":label3,"Itunes_url":itunes_url})
#    print(excel2)
    try:
        excel2['Label'] = excel2['Label'].map(lambda x: x.encode('unicode-escape').decode('utf-8'))
    except:
        pass
    try:
        excel2.to_csv("smit.csv", encoding='utf-8', index=False)
    except:
        excel2.to_csv("smit.csv", index=False)
    # excel=pd.DataFrame({'Rank':position,'Track':track,'Artist':artist,"Number of Streams":streams,"Label":label3,"Itunes_url":itunes_url})
    # excel['Label'] = excel['Label'].map(lambda x: x.encode('unicode-escape').decode('utf-8'))
    # excel.to_csv("streaming_music_industry_trakcer.csv",encoding='utf-8',index=False)




