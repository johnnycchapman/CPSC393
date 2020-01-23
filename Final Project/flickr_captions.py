import flickrapi
import json
import csv

if __name__ == '__main__':
    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    secret = 'XXXXXXXXXXXXXXXXX'
    user_id = '44494372@N05'
    photoset_id = '72157648186433655'
    flickr = flickrapi.FlickrAPI(api_key, secret, format='parsed-json')

    # pulling photo ids from ISS album
    photos = flickr.photosets.getPhotos(api_key=api_key, photoset_id=photoset_id, user_id=user_id)
    photo_ids = []
    photos = photos['photoset']['photo']
    # creating list of photo ids
    for i in range(1, len(photos)):
        photo_ids.append(photos[i]['id'])

    #write to csv file
    with open('sentiment_data.csv', mode='w') as sentiment_file:
        writer = csv.writer(sentiment_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['date','filename','description'])

        # pulling description for each photo in album
        for i in range(1, len(photo_ids)):
            info = flickr.photos.getInfo(api_key=api_key, photo_id=photo_ids[i])
            info = info['photo']['description']['_content']
            info = json.dumps(info)
            info = info.split("\\n")
            if len(info) == 4:
                descriptions = info[0]
                filenames = info[2]
                dates = info[3]
                writer.writerow([dates, filenames, descriptions])
            else:
                continue 
