# DATA-ASSISTANT REPOSITORY: BRANCHES

```
*This repository contains a simple text-info generator, a numbers to letters encoder and a color palette generator.*
*These elements can be combined into one program if you're interested in training your own model, or toggling with the capabilities of these features to see what they can do all together. Feel free to suggest or assist with version two features! As it stands right now, everything in this repository is very basic, and still may have one or two bugs. They should be very simple fixes if you're interested in giving it a shot. If not, version two will hopefully take care of any issues!*
--
There is also an AI model meant to analyze sentiment but everything is still in rough draft territory. At most, the model can sometimes tell you if a color is warm or cool but I haven't used my dataset generator to create it's data yet. 

# About this repository as a whole....
There's nothing too difficult about the files themselves, and some of them are dependant on others while others can be completely self-efficient. 
None of the files are ridiculously huge, and you can actually put them together in the same file and import them!
You can generate your down encoding language, assign letters to values, generate a color palette with extensive logging!
Furthermore, both of those features can assist with the data assistant generator. 
I made this on the hope of stream lining my Machine Learning course work because I was spending quite a lot of time LOOKING for data.
I almost slapped myself when I realized I could write a program to generate the data for me.....
If you use the color data generator to train an AI model, I'd love to know how it goes!
``` 

Though my inline comments probably arent the __most__ verbose, I do think that they're sufficient at giving a general rundown. If you have any questions though, I've got an open door policy. 
I just know for me personally, I don't have time to sit all day and read papers. If I'm looking for tools to use, it's because I have something I need to do. However, I am including a general guide for each folder to pair with the TODO comments. [^1]

______
## MAIN FILES AND FUNCTIONS - BRANCH TWO
---------

### Imports.py (2nd branch, at top) 

  <-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>

   || This is for the AI model. As of right now, they only get about a mid-range score when they practice the dataset. 
   
   || It took me SO LONG to make that dataset that I ended up creating a color palette generator
   
   || with robust headers. This file will run seperate from all the others. Feel free to expand on it's functionality, 
   
   || or play around with the data generator and feed it some data!
```

  <-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>
  
PLEASE ALSO DOWNLOAD OR HAVE ACCESS TO:
THE 'sentimentalai.py' FOLDER NEAR THE BOTTOM OF THIS REPISTORY BRANCH. THIS FILE CONTAINS THE NECESSARY IMPORTS, BUT I BELIEVE THAT IS ALL THIS FILE KEEPS TO RUN SMOOTHLY

<-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>
```

### SentAImatplotlib.py (2nd branch, near middle)
<-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>
      
  This file provides a method of generating visualizations for the data. I think the form is relatively simple as of right now, V2 will be on it's way! 

### SentiV2Dataset.xlsx 
   <-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>
   
  Unfortunately, this is an xlsx file. I'd recommend opening it in google sheets and only saving it to a cloud space because it's very robust. However, you can also generate your own data structure! I used the data generator for this, so hopefully, it gives you a good sense of what you can do with it.
  
<-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>
### Main-textgenerator.py
   This file compiles information into a dataset. It actually generates tables and should pretty much be self-contained. You can import data from the color palette generator __AND/OR__ create your own! 
   I don't have any how-to documents, I'll work on those and release them soon! 
   
  <-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>

  [^1] some items on branch 2 are also on branch one. I, therefore, will not explain them in an attempt to keep redudancy down.
  
### Textencoder.py
<-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-*-*>
  Not to sound rude but it encodes words! I don't think I implemented number-conversions yet but it's in the plans! 
  This file is also able to run on it's own. 
  
 *Thanks!*
 
