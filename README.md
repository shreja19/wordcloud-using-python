# wordcloud-using-python

Problem statement - creating a wordcloud using python libraries.

Here, I am using Pride and Prejudice book from project Gutenburg website for creating wordcloud.

Following are the important steps to do create wordcloud using object oriented version. 
Here, I have created a class named Book and it has various member functions and attributes,constructors as follows-

1. A constructor taking in the text file name, and representation method
2. Provide properties for getting and setting the actual book name (Pride and Prejudice in our case), and a getter for number of characters in the book
3. Provide member functions for: 1. removing punctuation marks,non-alphabetical characters, special characters, white spaces 2. stemming, 3. lemmatization, 4. stop word removal, and 5. word frequency computations
4. Provide member functions for word cloud display, and display of a bar graph showing frequency of occurrence of top 20 words
5. Provide a member function for sentiment visualizer that displays the sentiment of the book based on sentences. It will be a line display. The x axis will show the sentence number (starting at 0) and y-axis will display the sentiment and subjectivity as line graphs with a legend using two different colored lines for each.


