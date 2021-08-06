import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

uploader = fileupload.FileUploadWidget()

def _handle_upload(change):
    w = change['owner']
    with open(w.filename, 'wb') as f:
        f.write(w.data)
    print('Uploaded `{}` ({:.2f} kB)'.format(w.filename, len(w.data) / 2 **10))

uploader.observe(_handle_upload, names='data')

display(uploader)

#def calculate_frequencies(file_contents):


# file_contents = "the great gatsby! How is a (Everything). How do you do if her love isn't [the] great &^%#^ {}"

# def calculate_frequencies(file_contents):

#     content = file_contents
    
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
#     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
#     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
#     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#     modified_word = "".join(item for item in content if item not in punctuations)

#     querywords = modified_word.split()

#     resultwords = [word for word in querywords if word.lower() not in uninteresting_words]
#     result = " ".join(resultwords)

#     print(result)

#     cloud = wordcloud.WordCloud()
#     cloud.generate_from_frequencies(result)
#     return cloud.to_array()

# myimage = calculate_frequencies(file_contents)
# plt.imshow(myimage, interpolation = 'nearest')
# plt.axis('off')
# plt.show()