---
hide:
  - navigation
---

# Heroku vs Netfliy vs Vercel vs GitHub Pages vs Firebase vs Vercel

## Heroku vs Netlify
Heroku is a PaaS provider that offers hosting solutions for backend applications. Most of the popular backend programming languages like Python, Java and Ruby can be deployed on Heroku. Netlify on the other hand provides hosting for static sites and serverless backend services for frontend applications. 

Consider Heroku if you’re looking to deploy a backend application like a REST API. 
Consider using Netlify if you want to deploy a static site or add a new feature (serverless function) to an already existing frontend project.

## Netlify vs Vercel
Netlify is a cloud computing company that focuses on providing hosting solutions for frontend applications whilst Vercel is a collaboration and deployment platform for frontend developers. Both companies offer serverless backend services but there are some differences worth noting before choosing your desired service provider.

Netlify uses AWS lambda functions for its serverless functions feature and Vercel has a fair usage policy that restricts you from using their services for CPU intensive tasks like machine learning and crypto mining programs. Furthermore, Vercel also requires all [commercial usage](https://vercel.com/docs/platform/fair-use-policy#commercial-usage) to be on a paid plan. 

Consider using Netlify if you’re just starting out and want to serve a commercial site as well as save some buck. Consider Vercel if your project isn’t going to be partly or wholly CPU intensive.

## GitHub Pages vs Netlify
GitHub Pages allows you to host static sites straight from your GitHub repository whilst Netlify is a company solely created to meet static site hosting and serverless backend needs from all popular version control companies.

Consider GitHub Pages if you don’t plan on having any dynamic functionality on your site and are using GitHub for version control. You should also consider GitHub Pages if you’re not looking to sign up to a hosting service provider for your static site hosting needs as it uses your GitHub account for this. 

Consider Netlify if you are not using GitHub for version control or if your site will have some serverless backend features.

## Firebase vs Netlify
Firebase is Google’s platform for creating and hosting web and mobile software while Netlify is predominantly built to host web applications and serverless functions for frontend sites. Both platforms offer serverless functions as a service but firebase’s functions can only be written in JavaScript and TypeScript whereas Netlify functions can also be written in Go on top of the two languages that firebase supports. 

Netlify also offers teams a chance to collaborate on projects on their platform whereas firebase wasn’t built with teams in mind. Firebase has a built in database (Realtime or Firestore) that comes with it whereas if you want to use a database with Netlify you have to add the FaunaDB to your architecture as an add-on. 

Consider firebase if you’d like to use a database for your project and don’t want the extra step of adding add-ons to it. Consider using Netlify if you’d like to write your serverless functions in Go.

## Firebase vs Heroku 
Firebase is a platform where you can create and host common features for a web or mobile app like authentication, serverless functions and a database in addition to hosting frontend sites. Heroku on the other hand only focuses on providing hosting solutions for backend applications like API’s for example. 

Consider using firebase if you want to host a frontend site, use serverless functions, add user auth or a database to your project without having to worry about deploying the auth system or database. Consider Heroku if you want to deploy a backend application or host a database.

## Heroku vs Vercel
Heroku is a cloud computing platform that offers backend developers the chance to build and host their applications whilst Vercel is a platform where frontend developers can collaborate and host their static sites. The two provide hosting solutions for different products and Vercel also offers serverless backend services which allow the developer to only worry about writing backend code and not its deployment or server maintenance.

Consider Heroku if you’re looking to host a backend application or database and consider Vercel if you’re looking to host a frontend site or deploy a serverless function.

## Firebase vs Vercel
Firebase is a platform where you can host static sites as well as create and host serverless backend features for them whilst Vercel is a team oriented platform for frontend developers that allows them to integrate their changes and host the finished site and serverless functions on their infrastructure. 

Furthermore, firebase comes with two persistent ready to use databases (Realtime and Firestore) for your project whereas with Vercel you first have to connect to an external database, if you need one which might be in a different region than your app thereby introducing a latency risk. 

Consider using Firebase if you’re not working as a team or need to get a database working for your project as fast as possible with no latency risk. It is worth noting that Vercel charges you per team member per month so consider Vercel if you’re working as a team and don’t have a tight budget. 

## GitHub Pages vs Vercel
GitHub Pages is a free hosting solution for static sites using GitHub for version control while Vercel is a platform for hosting frontend sites from all the popular version control systems. In addition, Vercel also offers serverless backend services to its customers and has a pay as you grow model for the project you’ll be hosting with them.

Consider GitHub Pages if you’re looking to deploy a static site for free or don’t want to sign up for another service for your hosting needs as GitHub Pages uses your GitHub account to deploy the site. Consider Vercel if you’re looking to deploy a site which doesn’t use GitHub for version control or want to add serverless functions to your site. 

## GitHub Pages vs Heroku
GitHub Pages is a GitHub feature that allows you to freely serve static sites from GitHub repositories whilst Heroku is a cloud platform for hosting dynamic applications written in any of the popular backend programming languages like Ruby, Python, Java etc. Also, GitHub Pages only works with GitHub for version control whereas Heroku is flexible enough to work with all the major version control systems. 

Consider GitHub Pages if you want to host a static site for free and consider Heroku if you’re looking to host a backend application or database.
