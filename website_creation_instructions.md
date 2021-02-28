# Websites II: In Class Exercise 

## Overview 
Last class, you learned the basics of HTML and constructed a simple web page.
As we discussed, the power of the web is in the links to other sites and what those links reveal.
Today, we’re going to build a website, or a whole collection of pages.

Each of you is going to create a single page and then we’re going to link them together.
We will use [repl.it](repl.it) again.
We will use the resulting text and link structure later when we learn about algorithms. 
The data that we will use comes from a database that we will work with extensively during our SQL and databases module.   

## Scenario
Northwind Traders is a gourmet food distributor that started as a mail order company, but is trying to move onto the web (a little late, I know).
You’ve been hired as marketing consultant and web developer to help move them into the digital age. 
Creating a product-specific web page 
To start, we’re going to make a single page for each of the products currently carried by Northwind.
The list of Northwind’s products is [here](https://docs.google.com/spreadsheets/d/1u4DkBooPizE-Af4pkdZZrGHKyppx9VBUVU45ZnI_7do/edit#gid=2082189938).

## Assigning products 
Once you have your product, make a note of it here w/ your first name in the “Consultant” category:  

Add you info here:
*** Add your own URL Google Sheet here **

## Building your web page

For your product, built a page with the following characteristics: 
- The HTML title (<title></title>) with the full name of your product 
- An h1 heading with the full name of your product 
- A photo of the product (do a google search - as it is fictitious product, obviously the brand will not match).
Size the photo so that is 200 vertical pixels & as many horizontal pixels as needed to keep the image correctly sized
- Create an h2 heading titled “Product description” 
Under this heading, write a short paragraph describing the product in an appetizing way. User the “<p></p>” HTML tag to create a paragraph. The written description of the  product, emphasizing that product's taste profile (sour, sweet, salty, savory, crispy, smooth, etc.). 
- Create an h2 heading titled “Product Details” 
Under this h2 heading, create an unordered list with the pricing information, order quantity and supplier info (all available from the spreadsheet).  
- Create an h2 heading titled “Other product by this seller” 
Create an ordered list of all other products by this particular supplier (see the spreadsheet to look up the supplier & then find their other products). If another student created a page for that product, create a link to that product in the list.  

## Recommended pairings section 
Once the basic pages are created, we’re going to create a new h2 sub-section for each product called “Pairings” that will have links to other Northwind products that would go well with the particular product, as well as some accompanying ad copy. For example, your pairings copy might be (wrapped in a paragraph block): 

```
“Enjoy your delicious Wimmers gute Semmelknödel (a kind of bread-based German dumpling) with a class of delicious Rhönbräu Klosterbier (a German “cloister beer” i.e., one traditionally brewed by monks). For a special treat, try smothering your Wimmers gute Semmelknödel in Original Frankfurter grüne Soße” 
```

Recall how we link pages:
<a href="URL to other product page">Outback Lager</a>





