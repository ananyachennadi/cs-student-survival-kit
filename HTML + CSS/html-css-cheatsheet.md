# HTML + CSS Cheatsheet

# Introduction to HTML + CSS

The 3 core technologies for web development:

- **HTML** → Structure & Content
    
    *Example: text, buttons, images*
    
- **CSS** → Styling & Layout
    
    *Controls colours, fonts, positioning, etc.*
    
- **JavaScript** → Interactivity & Logic
    
    *Example: handle button clicks, form validation*
    

# HTML

## HTML basics

A HTML element represents a piece of content inside a webpage

Each element has an opening tag `<tagname>` and closing tag `</tagname>`

```html
<p>
	paragraph
</p>
<button>Hello</button>

<!-- href="" is a HTML attribute (modifies how an element behaves) -->
<!-- the target="_blank" attribute opens the link in a new tab -->

<a href="https://www.youtube.com/">
	anchor element (link to another website)
</a>
```

## The HTML structure

```html
<!DOCTYPE html>
<html> <!--tells the browser there is a web page inside the element-->
    
    <head> 
        <!--the head element contains meta-information about the web page-->
				
				<title>Youtube.com Clone</title> 
				<!-->changes the name of the tab-->
    </head>

    <body> 
        <!--the body element contains the content of the web page-->
    </body>
</html>
```

<aside>
🚨

If you do not use the `<style>` element and instead choose to create a new .css file, make sure you load the new .css file into the .html file

</aside>

You can do this by using a `<link>` element which is a void element (does not need a closing tag)

```html
<link rel="stylesheet" href="buttons.css">
<link rel="stylesheet" href="styles/buttons.css">
```

## Images and Text Boxes

```html
<style>
	.thumbnail {
		width: 300px;
		height: 300px;
		object-fit: cover; /* Ensures the image covers the entire area */
		object-position: right; /* Aligns the image to the right */
	}
</style>

<img class="thumbnail" src="thumbnails/thumbnail1.webp">
```

```html
<input type="text" placeholder="Search">
```

## The `<div>` element

The `<div>` element is a container (just a box) used to group elements together and is a block element by default

```html
<style>
	.div-element{
		
	}
</style>

<div class="div-element">
	
</div>
```

## Running JavaScript in HTML

The `<script>` element is used to include **JavaScript code** inside your HTML file.

`<script>` is placed at the bottom of <body> so that the HTML loads first and then JS is run to make it interactive.

```html
<body>
	<script>
		alert('hello');
	</script>
</body>
```

# CSS (Cascading Style Sheets)

## CSS basics

To use CSS styling you need a `<style>` tag in your HTML code

```html
<style>
    button{
        background-color: rgb(188, 9, 9); /*Red background*/
        color: white; /*White text*/
        border: none; /*No border*/
        height: 36px; /*Height of the button*/
        width: 105px; /*Width of the button*/
        border-radius: 2px; /*Rounded corners*/
        cursor: pointer; /*Pointer cursor on hover*/
    }
</style>

<button>SUBSCRIBE</button>
```

However say you have buttons that need different styles, you make classes of styles and implement it like below:

```html
<style>
    .subscribe-button {
        background-color: rgb(188, 9, 9);
        color: white;
        border: none;
        height: 36px;
        width: 105px;
        border-radius: 2px;
        cursor: pointer;
        /* the code below adds margin (space) around the button element */
				margin-right: 8px;
    }
    .join-button{
        background-color: transparent;
        color: rgb(28, 102, 192);
        border-color: rgb(28, 102, 192);
        height: 36px;
        width: 60px;
        border-radius: 2px;
        cursor: pointer;
        border-style: solid;
        border-width: 1px;        
    }
</style>

<button class="subscribe-button">SUBSCRIBE</button>
<button class="join-button">JOIN</button>
```

## Hovers, Transitions, Shadows

These refer to the style changing when a mouse hovers over it and the way to implement this is `.className : hover{ }`

This is known as a pseudo-class (add extra styles in a certain situation)

Another example of a pseudo-class is `.className: active{ }` which defines the style when an element is clicked

```css
.join-button:hover{
        background-color: rgb(48, 22, 140);
        color: white;
}
.join-button:active{
        opacity: 0.7;
}
```

We also need to make the transition smooth instead of immediate

```css
.join-button{
        background-color: transparent;
        color: rgb(28, 102, 192);
        border-color: rgb(28, 102, 192);
        height: 36px;
        width: 60px;
        border-radius: 2px;
        cursor: pointer;
        border-style: solid;
        border-width: 1px;
        margin-right: 8px;
        /*Transition for smooth hover effect*/
        transition: background-color 0.3s, color 0.3s;
    }
```

```css
.tweet-button:hover{
        box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.15);
    }
```

## Chrome DevTools

Chrome DevTools is a really useful way to learn HTML and CSS

Right-click on any page in Chrome and select **“Inspect”** which opens the **Elements** panel

Click the hover icon to highlight any element on the page and DevTools will show you their layout and CSS

The **Computed** tab will show you the element’s final style

## CSS Box Model

If you set the height and the width what can happen sometimes is the text might not fit within the box so instead you can add spacing on the inside

```css
.join-button{
        padding-left: 10px;
        padding-right: 10px;
        padding-top: 9px;
        padding-bottom: 9px;
    }
```

## Text Styles

You can use fonts other than the default fonts by using Google Fonts

Select the font you want as well as the styles you want and copy the html and add it to the head section of your code

```css
<style>
    .video-title{
        font-family: Arial, Helvetica, sans-serif;
        font-size: 18px;
        font-weight: bold;
        width: 300px;
        line-height: 24px; 
        margin-bottom: 0px;
    }

    .video-stats{
        font-family: Arial, Helvetica, sans-serif;
        font-size: 14px;
        color: #606060;
        width: 300px;
        line-height: 20px; 
        margin-top: 2px;
    }
</style>

<p class="video-title">
    Talking Tech and Ai with Google CEO Sundar Pichai!
</p>

<p class="video-stats">
    3.4M views &#183; 6 months ago
</p>
```

The `<strong>` `</strong>` element makes text bold

The `<u>` `</u>` element creates text that is underlined

The `<span>` `</span>` element creates text with no styles applied

All of these can have classes specified

e.g. `<span class=””>` `</span>`

## CSS Display Property

There are three types of elements in HTML:

- ***Block element*** (takes up an entire line e.g. `<p>`)
    
    Even if you change the width, block elements will still take up the entire line
        

- ***Inline-block element*** (only takes up as much space as needed e.g. `<img>`, `<input>`)
- ***Inline element*** (appear within a line of text e.g. `<strong>)`

You can switch between these types

```html
<style>
	.video-author, .video-stats{
		display: inline-block;
	}
</style>

<p class="video-author">
	Marques Brownlee
</p>
<p class="video-stats">
	3.4M views
</p>
```

## Nested Layouts Technique

There are two types of layouts:

- Vertical Layout
- Horizontal Layout

Each section is its own `<div>` element

```html
<style>
	.profile-picture{
		width: 100%; /*pictures fills up the size of the div*/
	}
</style>

<div class = "channel-picture">
	<img class = "profile-picture" src="">
</div>
```

## CSS Grid

CSS Grid is a layout system that allows you to create layouts by defining **rows and columns** directly on a container

As you can see if there are more <div> elements than columns they get added to a new row

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Grid Practise</title>
    </head>
    <body>
        <div style="
            display: grid;
            grid-template-columns: 100px 100px; 
            /* Defines two columns each 100px wide */
        ">
            <div style="background-color: lightblue;">
                div1
            </div>
            <div style="background-color: lightpink;">
                div2
            </div>
            <div style="background-color: lightgreen;">
                div3
            </div>
        </div>
    </body>
</html>
```

```html
<div style="
    display: grid;
    grid-template-columns: 100px 1fr; 
    /*1fr means take up the rest of the spad in the grid*/
 ">
```

```html
<div style="
    display: grid;
    grid-template-columns: 100px 1fr 2fr; 
    /* This creates a grid with three columns: the first is 100px wide,
    the second takes up 1 fraction of the available space,
    and the third takes up 2 fractions of the available space. */
">
```

For images, they take their original size so to fit it in a container:

```css
.thumbnail{
	width: 100%;
}
```
