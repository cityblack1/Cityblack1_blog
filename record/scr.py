import re
html = '''<!DOCTYPE
html >
< html
lang = "zh-cn"


class ="js" >

< head > < meta
http - equiv = "Content-Type"
content = "text/html; charset=UTF-8" >
< link
rel = 'shortcut'
href = / static / favicon.ico / >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1" >
< script > (function(html)
{html.className = html.className.replace( /\bno - js\b /, 'js')})(document.documentElement); < / script >
< title
style = '"Arial","Microsoft YaHei","黑体","宋体",sans-serif;' > Home - 褐色城市 < / title >
< link
rel = "stylesheet"
id = "twentysixteen-jetpack-css"
href = "/static/twentysixteen.css"
type = "text/css"
media = "all" >

< link
rel = "stylesheet"
id = "genericons-css"
href = "/static/genericons.css"
type = "text/css"
media = "all" >

< link
rel = "stylesheet"
href = "/static/css_custom/form_check.css"
type = "text/css" >
< link
rel = "stylesheet"
href = "/static/highlights/default.css"
type = "text/css" >
< script
src = "http://libs.baidu.com/jquery/1.7.2/jquery.min.js" > < / script >

< link
rel = "stylesheet"
id = "twentysixteen-style-css"
href = "/static/style(1).css"
type = "text/css"
media = "all" >
< link
rel = "stylesheet"
id = "jetpack-top-posts-widget-css"
href = "/static/css_custom/bread.css"
type = "text/css"
media = "all" >
< link
rel = "stylesheet"
id = "twentysixteen-style-css"
href = "/static/css_custom/boots.css"
type = "text/css" >

< link
rel = "stylesheet"
id = "sharedaddy-css"
href = "/static/sharing.css"
type = "text/css"
media = "all" >
< link
rel = "stylesheet"
id = "social-logos-css"
href = "/static/social-logos.min.css"
type = "text/css"
media = "all" >

< script
type = "text/javascript"
src = "/static/js/forms_check.js" > < / script >

< link
rel = "stylesheet"
href = "/static/display/css/component.css"
type = "text/css" >
< link
rel = "stylesheet"
href = "/static/display/css/default.css"
type = "text/css" >

< script >
// this is important
for IEs
  var
  polyfilter_scriptpath = '/static/display/js';
$(document).ready(function()
{
  var
next_url = '/';
$('.next').attr('value', next_url);
$(".close-message").bind("click", function()
{
$("#modal-2").removeClass('md-show')
});
});
< / script >
< / head >

< body


class ="home blog hfeed infinite-scroll neverending" >


1

< div


class ="md-modal md-effect-1" id="modal-15" >

< div


class ="md-content" >

< h3 > LOG
OUT < / h3 >
< div >
< div


class ="modal-dialog modal-sm" >

< div


class ="modal-content" >

< form
id = "logout_form"
action = "/users/logout/"
method = "POST" >
< input
type = 'hidden'
name = 'csrfmiddlewaretoken'
value = 'wPHttV6JOBoYTchxjdvCMPtCLvXsE9L4SXS7gOSjZIVkGpKpfsFukhUfRSaxYebn' / >
< div


class ="modal-header" >

< h4


class ="modal-title" id="RegisterModalLabel" >

< / h4 >
< / div >

< div


class ="modal-body" >

< div


class ="control-group" style="color: #000" >

< label


class ="control-label" for ="reg_pwd2" > 您确定要登出吗? < / label >

< / div >

< p
id = "reg_tip"
style = "color:red;" > < / p >
< / div >

< div


class ="modal-footer" >

< input
type = "hidden"


class ="next" id='next' name="next" / >

< input


class ="btn btn-primary" value="LOGOUT" type="submit" >

< / div >
< / form >
< / div > <!-- /.modal - content -->
< / div > <!-- /.modal -->
< / div >
< div
style = "padding-bottom: 1em;background: rgba(0, 0, 0, 0.16);" >
< button


class ="md-close" style="background: rgba(0, 0, 0, 0.53)" > Close me! < / button > < / div >

< / div >
< / div >

< div
id = "page"


class ="site" >

< div


class ="site-inner" >

< header
id = "masthead"


class ="site-header" role="banner" >

< div


class ="site-header-main" >

< div


class ="site-branding" >

< h1


class ="site-title" >

< a
href = "http://localhost:8000"
rel = "home" > 褐色城市 < / a > < / h1 >
< p


class ="site-description" > The website of Cityblack1 < / p >

< / div > <!--.site - branding -->

< button
id = "menu-toggle"


class ="menu-toggle" > Menu < / button >

< div
id = "site-header-menu"


class ="site-header-menu" >

< nav
id = "site-navigation"


class ="main-navigation" role="navigation" aria-label="Primary Menu" >

< div


class ="menu-sections-container" >

< ul
id = "menu-sections"


class ="primary-menu" >

< li
id = "menu-item-3829"


class ="menu-item menu-item-type-post_type menu-item-object-page menu-item-3829" > < a href="None" > About me < / a > < / li >

< li > < a
href = "#" > Producting... < / a > < / li >
< li > < a
href = "#" > Producting... < / a > < / li >
< li > < a
href = "#" > Producting... < / a > < / li >
< / ul > < / div > < / nav > <!--.main - navigation -->

< / div > <!--.site - header - menu -->
< / div > <!--.site - header - main -->

< div


class ="header-image" >

< a
href = "http://localhost:8000"
rel = "home" >
< img
alt = "褐色城市"
src = "http://owdakhn64.bkt.clouddn.com/header.png" >
< / a >
< / div > <!--.header - image -->
< / header > <!--.site - header -->

< hr
id = "page_anchor"
style = "border: 0;height: 0" >
< div
id = "content"


class ="site-content" >

< div
id = "primary"


class ="content-area" >

< main
id = "main"


class ="site-main" role="main" >

< div


class ="wagtail-userbar-reset" >

< div


class ="wagtail-userbar wagtail-userbar--bottom-right no-touch" data-wagtail-userbar="" >

< link
rel = "stylesheet"
href = "/static/wagtailadmin/css/userbar.css"
type = "text/css" >
< div


class ="wagtail-userbar-nav" >

< div


class ="wagtail-icon wagtail-icon-wagtail wagtail-userbar-trigger" data-wagtail-userbar-trigger="" >

< span


class ="wagtail-userbar-help-text" > Go to Wagtail admin interface < / span >

< / div >
< div


class ="wagtail-userbar-items" >

< div


class ="wagtail-userbar__item " >

< div


class ="wagtail-action wagtail-icon wagtail-icon-wagtail" >

< a
href = "/admin/"
target = "_parent"


class ="" > Go to Wagtail admin < / a >

< / div >
< / div >

< div


class ="wagtail-userbar__item " >

< div


class ="wagtail-action wagtail-icon wagtail-icon-folder-open-inverse" >

< a
href = "/admin/pages/1/"
target = "_parent" > Show in Explorer < / a >
< / div >
< / div >

< div


class ="wagtail-userbar__item " >

< div


class ="wagtail-action wagtail-icon wagtail-icon-edit" >

< a
href = "/admin/pages/3/edit/"
target = "_parent" > Edit
this
page < / a >
< / div >
< / div >

< div


class ="wagtail-userbar__item " >

< div


class ="wagtail-action wagtail-icon wagtail-icon-plus" >

< a
href = "/admin/pages/3/add_subpage/"
target = "_parent" > Add
a
child
page < / a >
< / div >
< / div >

< / div >
< / div >
< script
src = "/static/wagtailadmin/js/userbar.js" > < / script >
< / div >
< / div >

< article


class ="post type-post status-publish format-standard hentry category-uncategorized" >

< header


class ="entry-header" >

< h2


class ="entry-title" > < a href="/%E6%B5%8B%E8%AF%95/%E6%B5%8B%E8%AF%95%E5%8D%9A%E5%AE%A2%E4%B8%80/" rel="bookmark" > 测试博客一 < / a > < / h2 >

< / header > <!--.entry - header -->
< div


class ="entry-content" >

< div


class ="codehilite" > < pre > < span > < / span > python


this is a
test
< / pre > < / div >

< p > < / p >
< p > < a
href = "/%E6%B5%8B%E8%AF%95/%E6%B5%8B%E8%AF%95%E5%8D%9A%E5%AE%A2%E4%B8%80/" > < button


class ="btn-4" > Continue Reading...< / button > < / a > < / p >

< div


class ="sharedaddy sd-sharing-enabled" >

< div


class ="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing" >

< h3


class ="sd-title" > Share this:<

  / h3 >
< div


class ="sd-content" >

< ul >
< li


class ="share-google-plus-1" >

< a
rel = "nofollow"
data - shared = "sharing-google-4001"


class ="share-google-plus-1 sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=google-plus-1&amp;nb=1" target="_blank" title="Click to share on Google+" > < span > Google < / span > < / a > < / li >

< li


class ="share-linkedin" >

< a
rel = "nofollow"
data - shared = "sharing-linkedin-4001"


class ="share-linkedin sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=linkedin&amp;nb=1" target="_blank" title="Click to share on LinkedIn" > < span > LinkedIn < / span > < / a > < / li >

< li


class ="share-facebook" > < a rel="nofollow" data-shared="sharing-facebook-4001" class ="share-facebook sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=facebook&amp;nb=1" target="_blank" title="Click to share on Facebook" > < span > Facebook < / span > < / a > < / li > < li class ="share-twitter" > < a rel="nofollow" data-shared="sharing-twitter-4001" class ="share-twitter sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=twitter&amp;nb=1" target="_blank" title="Click to share on Twitter" > < span > Twitter < / span > < / a > < / li > < li > < a href="http://krondo.com/#" class ="sharing-anchor sd-button share-more" > < span > More < / span > < / a > < / li > < li class ="share-end" > < / li > < / ul >

< div


class ="sharing-hidden" >

< div


class ="inner" style="display: none;" >

< ul > < li


class ="share-reddit" >

< a
rel = "nofollow"
data - shared = ""


class ="share-reddit sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=reddit&amp;nb=1" target="_blank" title="Click to share on Reddit" > < span > Reddit < / span > < / a > < / li > < li class ="share-tumblr" > < a rel="nofollow" data-shared="" class ="share-tumblr sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=tumblr&amp;nb=1" target="_blank" title="Click to share on Tumblr" > < span > Tumblr < / span > < / a > < / li > < li class ="share-end" > < / li > < li class ="share-pinterest" > < a rel="nofollow" data-shared="sharing-pinterest-4001" class ="share-pinterest sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=pinterest&amp;nb=1" target="_blank" title="Click to share on Pinterest" > < span > Pinterest < / span > < / a > < / li > < li class ="share-print" > < a rel="nofollow" data-shared="" class ="share-print sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/" target="_blank" title="Click to print" > < span > Print < / span > < / a > < / li > < li class ="share-end" > < / li > < li class ="share-email share-service-visible" > < a rel="nofollow" data-shared="" class ="share-email sd-button share-icon" href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/?share=email&amp;nb=1" target="_blank" title="Click to email this to a friend" > < span > Email < / span > < / a > < / li > < li class ="share-end" >

< / li >
< / ul >
< / div >
< / div >
< / div >
< / div >
< / div >
< / div >
< footer


class ="entry-footer" >

< span


class ="posted-on" >

< a
href = "/"
rel = "author" > cityblack1 < / a >
< / span >
< span


class ="posted-on" >

< span


class ="screen-reader-text" > Posted on < / span > < a href="/" rel="author" > cityblack1 < / a >

< / span >
< span


class ="posted-on" >

< span


class ="screen-reader-text" > Posted on < / span > < a href="/" rel="date" > 2017年9月21日 < / a >

< / span >
< span


class ="posted-on" >

< span


class ="screen-reader-text" > Posted on < / span > < a href="/" rel="categoty" > 测试 < / a >

< / span >
< span


class ="comments-link" > < a href="http://krondo.com/review-the-undoing-project-a-friendship-that-changed-our-minds/#respond" > Leave a comment < span class ="screen-reader-text" > on Review: The


Undoing
Project: A
Friendship
That
Changed
Our
Minds < / span > < / a > < / span >
< / footer > <!--.entry - footer -->
< / article > <!--  # post-## -->
< br >
< br >

< br > < br >

< / main > <!--.site - main -->
< / div > <!--.content - area -->

< aside
id = "secondary"


class ="sidebar widget-area" role="complementary" >

< section
id = "meta-3"


class ="widget widget_meta" > < h2 class ="widget-title" > Meta < / h2 >

< button


class ="md-trigger" data-modal="modal-15" > LOG & nbsp; OUT < / button >

< ul >
< li > < a
href = "http://localhost:8000" > Back
to
Home < / a > < / li >
< li > < a
href = "#" > Leave
me
a
message < / a > < / li >
< li > < a
href = "#" > User
center < / a > < / li >

< / ul >
< / section > < section
id = "search-3"


class ="widget widget_search" >

< form
role = "search"
method = "get"


class ="search-form" action="/search/#page_anchor" >

< label >
< span


class ="screen-reader-text" > Search for:<

  / span >
< input
type = "search"


class ="search-field" placeholder="Search …" value="" name="query" >

< / label >
< button
type = "submit"


class ="search-submit" > < span class ="screen-reader-text" > Search < / span > < / button >

< / form >
< / section >

< section
id = "nav_menu-3"


class ="widget widget_nav_menu" >

< h2


class ="widget-title" > CATEGORY < / h2 >

< div


class ="menu-sections-container" >

< ul
id = "menu-sections-1"


class ="menu" >

< li


class ="menu-item menu-item-type-post_type menu-item-object-page" > < a href="/%E6%B5%8B%E8%AF%95/?c=测试#page_anchor" > 测试 & nbsp; & nbsp;(1) < / a > < / li >

< / ul > < / div > < / section >

< section
id = "top-posts-2"


class ="widget widget_top-posts" >

< h2


class ="widget-title" > DATE & nbsp;RECORD < / h2 >

< ul >

< li >

< a
href = "/search/?date=2017m9#page_anchor"


class ="bump-view" data-bump-view="tp" >


2017
年
9
月 & nbsp; & nbsp; & nbsp;
( & nbsp;
1 & nbsp;)
< / a >

< / li >

< / ul >
< / section >
< section
id = "linkcat-2"


class ="widget widget_links" >

< h2


class ="widget-title" > TAGS < / h2 >

< ul


class ="xoxo blogroll" >

< / ul >
< / section >
< section
id = "blog_subscription-3"


class ="widget jetpack_subscription_widget" >

< h2


class ="widget-title" > Subscribe to Blog via Email < / h2 >

< form
action = "#"
method = "post"
accept - charset = "utf-8"
id = "subscribe-blog-blog_subscription-3" >
< div
id = "subscribe-text" > < p > This
feature is under
testing... < / p >
< / div > < p > Join
0
other
subscribers < / p >
< p
id = "subscribe-email" >
< label
id = "jetpack-subscribe-label"
for ="subscribe-field-blog_subscription-3" style="clip: rect(1px 1px 1px 1px); position: absolute; height: 1px; width: 1px; overflow: hidden;" >
Email
Address < / label >
< input
type = "email"
name = "email"
required = "required"


class ="required" value="" id="subscribe-field-blog_subscription-3" placeholder="Email Address" >

< / p >

< p
id = "subscribe-submit" >
< input
type = "submit"
value = "Subscribe"
name = "jetpack_subscriptions_widget" >
< / p >
< / form >

< script >
/ *
Custom
functionality
for safari and IE
  * /
  (function(d)
  {
  // In
  case
  the
  placeholder
  functionality is available
  we
  remove
  labels
  if (('placeholder' in d.createElement('input')))
  {
      var
  label = d.querySelector('label[for=subscribe-field-blog_subscription-3]');
  label.style.clip = 'rect(1px, 1px, 1px, 1px)';
  label.style.position = 'absolute';
  label.style.height = '1px';
  label.style.width = '1px';
  label.style.overflow = 'hidden';
  }

  // Make
  sure
  the
  email
  value is filled in before
  allowing
  submit
  var
  form = d.getElementById('subscribe-blog-blog_subscription-3'),
         input = d.getElementById('subscribe-field-blog_subscription-3'),
                 handler = function(event)
  {
  if ('' == = input.value ) {
      input.focus();

  if (event.preventDefault){
  event.preventDefault();
  }

  return false;
  }
  };

  if (window.addEventListener) {
  form.addEventListener( 'submit', handler, false );
  } else {
  form.attachEvent( 'onsubmit', handler );
  }
  })( document );
  < / script >

  < / section >
  < !-- Start of Kindle This Widget -->
  < section id="contact_me"


  class ="widget widget_kindle_this" > < h2 class ="widget-title" > Contact Me < / h2 > < div style="font-size:.9em;" >
< form
action = "http://krondo.com/"
method = "GET"
onsubmit = "kpg_kindle_it(this);return false;" >
< span
style = "color:red;font-weight:bold"
id = "kpg_kc_1" > < / span >
< fieldset
style = "border:thin black solid;padding:2px;" > < legend > Your
name: < / legend >
< input
style = "font-size:.9em;"
size = "32"
name = "kindle_email"
type = "text"
placeholder = "your-name" > < br > (Enter
the
nickname
you
like) < / fieldset >
< fieldset
style = "border:thin black solid;padding:2px;" > < legend > Your
E - mail: < / legend >
< input
style = "font-size:.9em;"
size = "32"
name = "from_email"
type = "text"
placeholder = "good@email" > < br > (Approved
E - mail
that
I
can
touch
you)
< / fieldset >
< fieldset
style = "border:thin black solid;padding:2px;" > < legend > Kindle
base
email < / legend >
< textarea
name = "contact-me"
title = "contact-me"
placeholder = "Enter you message here" > < / textarea >
< br > (example: cityblack1 is a
handsome
guy!)
< / fieldset >
< input
type = "submit"
name = "kpg_ksub"
value = "send to Cityblack1" >
< / form >
< / div >

< / section >
< !-- end
of
Kindle
This
Widget -->
< section
id = "archives-3"


class ="widget widget_archive" > < / section >

< / aside > <!--.sidebar.widget - area -->

< / div > <!--.site - content -->

< footer
id = "colophon"


class ="site-footer" role="contentinfo" >

< nav


class ="main-navigation" role="navigation" aria-label="Footer Primary Menu" >

< div


class ="menu-sections-container" >

< ul
id = "menu-sections-2"


class ="primary-menu" >

< li


class ="menu-item menu-item-type-post_type menu-item-object-page menu-item-3829" > < a href="None" > About me < / a > < / li >

< li


class ="menu-item menu-item-type-post_type menu-item-object-page menu-item-3713" > < a href="#" > Twisted Introduction < / a > < / li >

< li


class ="menu-item menu-item-type-post_type menu-item-object-page menu-item-3711" > < a href="#" > Programmer’s Editors < / a > < / li >

< li


class ="menu-item menu-item-type-post_type menu-item-object-page menu-item-3712" > < a href="#" > Software < / a > < / li >

< / ul > < / div > < / nav > <!--.main - navigation -->

< div


class ="site-info" >

< span


class ="site-title" > < a href="http://localhost:8000" rel="home" > 褐色城市 < / a > < / span >


by
Cityblack1
< / div > <!--.site - info -->
< / footer > <!--.site - footer -->
< / div > <!--.site - inner -->
< / div > <!--.site -->

< script
type = "text/javascript"
src = "/static/photon.js" > < / script >
< script
type = "text/javascript"
src = "/static/devicepx-jetpack.js" > < / script >
< script
type = "text/javascript" >
/ * < ![CDATA[* /

      var jetpackCarouselStrings = {
  "widths": [370, 700, 1000, 1200, 1400, 2000],
  "is_logged_in": "",
  "lang": "en",
  "ajaxurl": "http:\/\/krondo.com\/wp-admin\/admin-ajax.php",
  "nonce": "f7da50cca3",
  "display_exif": "1",
  "display_geo": "1",
  "single_image_gallery": "1",
  "single_image_gallery_media_file": "",
  "background_color": "black",
  "comment": "Comment",
  "post_comment": "Post Comment",
  "write_comment": "Write a Comment..."
};

/ *]] > * /
< / script >
< script
type = "text/javascript"
src = "/static/jetpack-carousel.js" > < / script >
< script
type = "text/javascript" >
/ * < ![CDATA[* /
      var mejsL10n = {"language": "en-US", "strings": {"Close": "Close", "Fullscreen": "Fullscreen",
                                                       "Turn off Fullscreen": "Turn off Fullscreen",
                                                       "Go Fullscreen": "Go Fullscreen",
                                                       "Download File": "Download File",
                                                       "Download Video": "Download Video", "Play": "Play",
                                                       "Pause": "Pause", "Captions\/Subtitles": "Captions\/Subtitles",
                                                       "None": "None", "Time Slider": "Time Slider",
                                                       "Skip back %1 seconds": "Skip back %1 seconds",
                                                       "Video Player": "Video Player", "Audio Player": "Audio Player",
                                                       "Volume Slider": "Volume Slider", "Mute Toggle": "Mute Toggle",
                                                       "Unmute": "Unmute", "Mute": "Mute",
                                                       "Use Up\/Down Arrow keys to increase or decrease volume.": "Use Up\/Down Arrow keys to increase or decrease volume.",
                                                       "Use Left\/Right Arrow keys to advance one second, Up\/Down arrows to advance ten seconds.": "Use Left\/Right Arrow keys to advance one second, Up\/Down arrows to advance ten seconds."}};
var
_wpmejsSettings = {"pluginPath": "\/wp-includes\/js\/mediaelement\/"};
/ *]] > * /
< / script >
< script
type = "text/javascript"
src = "/static/postmessage.js" > < / script >
< div
id = "likes-other-gravatars" > < div


class ="likes-text" > < span > % d < / span > bloggers like this:<

  / div > < ul


class ="wpl-avatars sd-like-gravatars" > < / ul > < / div >

< script
type = 'text/javascript'
src = '/static/comments/wpgroho.js' > < / script >

< div
style = "display:none" >
< / div >
< script
type = 'text/javascript' >
/ * < ![CDATA[* /
      var HighlanderComments = {"loggingInText": "Logging In\u2026", "submittingText": "Posting Comment\u2026",
                                "postCommentText": "Post Comment", "connectingToText": "Connecting to %s",
                                "commentingAsText": "%1$s: You are commenting using your %2$s account.",
                                "logoutText": "Log Out", "loginText": "Log In",
                                "connectURL": "https:\/\/jetpack.wordpress.com\/public.api\/connect\/?action=request",
                                "logoutURL": "https:\/\/jetpack.wordpress.com\/wp-login.php?action=logout&_wpnonce=11242c8adc",
                                "homeURL": "https:\/\/luminouscreaturespress.com\/", "postID": "14",
                                "gravDefault": "mystery", "enterACommentError": "Please enter a comment",
                                "enterEmailError": "Please enter your email address here",
                                "invalidEmailError": "Invalid email address",
                                "enterAuthorError": "Please enter your name here",
                                "gravatarFromEmail": "This picture will show whenever you leave a comment. Click to customize it.",
                                "logInToExternalAccount": "Log in to use details from one of these accounts.",
                                "change": "Change", "changeAccount": "Change Account", "comment_registration": "0",
                                "userIsLoggedIn": "", "isJetpack": "1", "text_direction": "ltr"};
/ *]] > * /
< / script >
< script
type = 'text/javascript'
src = '/static/comments/script.js' > < / script >
< script
type = 'text/javascript'
src = '/static/comments/reblog.js' > < / script >
< script
type = "text/javascript" >
< / script >

< link
rel = 'stylesheet'
id = 'all-css-0-2'
href = '/static/style(4).css'
type = 'text/css'
media = 'all' / >

< div
id = "sharing_email"
style = "display: none;" >
< form
action = "http://krondo.com/"
method = "post" >
< label
for ="target_email" > Send to Email Address < / label >
< input
type = "email"
name = "target_email"
id = "target_email"
value = "" >

< label
for ="source_name" > Your Name < / label >
< input
type = "text"
name = "source_name"
id = "source_name"
value = "" >

< label
for ="source_email" > Your Email Address < / label >
< input
type = "email"
name = "source_email"
id = "source_email"
value = "" >

< input
type = "text"
id = "jetpack-source_f_name"
name = "source_f_name"


class ="input" value="" size="25" autocomplete="off" title="This field is for validation and should not be changed" >

< img
style = "float: right; display: none"


class ="loading" src="/static/loading.gif" alt="loading" width="16" height="16" scale="0" >

< input
type = "submit"
value = "Send Email"


class ="sharing_send" >

< div


class ="errors errors-1" style="display: none;" >


Post
was
not sent - check
your
email
addresses! < / div >

< div


class ="errors errors-2" style="display: none;" >


Email
check
failed, please
try again < / div >

< div


class ="errors errors-3" style="display: none;" >


Sorry, your
blog
cannot
share
posts
by
email. < / div >
< / form >
< / div >
< img
src = "/static/g.gif"
alt = ":)"
width = "6"
height = "5"
id = "wpstats"
scale = "0" >
< / body >
< / html >

< script
type = "text/javascript"
src = "/static/display/js/classie.js" > < / script >

< script
type = "text/javascript"
src = "/static/display/js/modalEffects.js" > < / script >'''

a= """< title style = '"Arial","Microsoft YaHei","黑体","宋体",sans-serif;' > Home - 褐色城市 < / title >
"""

# < title
# style = '"Arial","Microsoft YaHei","黑体","宋体",sans-serif;' > Home - 褐色城市 < / title >
# < link

a = re.search('title.*?>(.*?)<', html, flags=re.S).group(1)

b = 1