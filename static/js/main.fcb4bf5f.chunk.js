(this["webpackJsonpreact-tutorial"]=this["webpackJsonpreact-tutorial"]||[]).push([[0],{23:function(e,t,a){},28:function(e,t,a){"use strict";a.r(t);var n=a(1),r=a(0),i=a(4),s=a.n(i),c=(a(23),a(15)),o=a(7),l=a(8),h=a(10),d=a(9),u=function(){return Object(n.jsx)("thead",{children:Object(n.jsxs)("tr",{children:[Object(n.jsx)("th",{children:"Variety"}),Object(n.jsx)("th",{children:"Seeding Outdoor"}),Object(n.jsx)("th",{children:"Seeding Indoor"}),Object(n.jsx)("th",{children:"Harvest"}),Object(n.jsx)("th",{children:"Exposition"}),Object(n.jsx)("th",{children:"Time to Harvest"}),Object(n.jsx)("th",{children:"Remove"})]})})},j=function(e){var t=e.characterData.map((function(t,a){return Object(n.jsxs)("tr",{children:[Object(n.jsx)("td",{children:t.variety}),Object(n.jsx)("td",{children:function(){var e="";return""!==t.seedingOutdoor[0]&&(e=JSON.stringify(t.seedingOutdoor.map((function(e){return e.label})))),e}()}),Object(n.jsx)("td",{children:function(){var e="";return""!==t.seedingIndoor[0]&&(e=JSON.stringify(t.seedingIndoor.map((function(e){return e.label})))),e}()}),Object(n.jsx)("td",{children:function(){var e="";return""!==t.harvest[0]&&(e=JSON.stringify(t.harvest.map((function(e){return e.label})))),e}()}),Object(n.jsx)("td",{children:t.exposition}),Object(n.jsx)("td",{children:t.timeToHarvest}),Object(n.jsx)("td",{children:Object(n.jsx)("button",{onClick:function(){return e.removeCharacter(a)},children:"Delete"})})]},a)}));return Object(n.jsx)("tbody",{children:t})},b=function(e){var t=e.characterData,a=e.removeCharacter;return Object(n.jsxs)("table",{children:[Object(n.jsx)(u,{}),Object(n.jsx)(j,{characterData:t,removeCharacter:a})]})},O=a(6),v=a(3),m=a(11),x=[{label:"January",value:"1"},{label:"February",value:"2"},{label:"March",value:"3"},{label:"April",value:"4"},{label:"May",value:"5"},{label:"June",value:"6"},{label:"July",value:"7"},{label:"August",value:"8"},{label:"September",value:"9"},{label:"October",value:"10"},{label:"November",value:"11"},{label:"December",value:"12"}],p=function(e){Object(h.a)(a,e);var t=Object(d.a)(a);function a(){var e;Object(o.a)(this,a);for(var n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return(e=t.call.apply(t,[this].concat(r))).initialState={variety:"",seedingOutdoor:[""],seedingIndoor:[""],harvest:[""],exposition:"",timeToHarvest:""},e.state=e.initialState,e.handleMonthChange=function(t,a){var n=a.name,r=t,i=[];if(null==r)e.setState(Object(O.a)({},n,""));else for(var s=0,c=r.length;s<c;s++)i.push(r[s].value);e.setState(Object(O.a)({},n,i))},e.handleMonthChange=function(t,a){var n=a.name;e.setState(Object(O.a)({},n,t))},e.handleChange=function(t){var a=t.target,n=a.name,r=a.value;e.setState(Object(O.a)({},n,r))},e.addForm=function(){e.props.handleSubmit(e.state),e.setState(e.initialState)},e}return Object(l.a)(a,[{key:"render",value:function(){var e=this.state,t=e.variety,a=e.seedingOutdoor,r=e.seedingIndoor,i=e.harvest,s=e.exposition,c=e.timeToHarvest;return Object(n.jsx)(n.Fragment,{children:Object(n.jsxs)(v.a,{children:[Object(n.jsxs)(v.a.Group,{children:[Object(n.jsx)(v.a.Label,{children:"Variety"}),Object(n.jsx)(v.a.Control,{type:"text",name:"variety",id:"variety",value:t,onChange:this.handleChange,placeholder:"Enter plant variety"}),Object(n.jsx)(v.a.Text,{className:"text-muted",children:"Please type plant variety"})]}),Object(n.jsx)(v.a.Label,{children:"Seeding Outdoor"}),Object(n.jsx)(m.a,{name:"seedingOutdoor",id:"seedingOutdoor",options:x,value:a,isMulti:!0,onChange:this.handleMonthChange}),Object(n.jsx)(v.a.Label,{children:"Seeding Indoor"}),Object(n.jsx)(m.a,{name:"seedingIndoor",id:"seedingIndoor",options:x,value:r,isMulti:!0,onChange:this.handleMonthChange}),Object(n.jsx)(v.a.Label,{children:"Harvest"}),Object(n.jsx)(m.a,{name:"harvest",id:"harvest",options:x,value:i,isMulti:!0,onChange:this.handleMonthChange}),Object(n.jsxs)(v.a.Group,{children:[Object(n.jsx)(v.a.Label,{children:"Exposition"}),Object(n.jsxs)(v.a.Control,{as:"select",name:"exposition",id:"exposition",value:s,onChange:this.handleChange,children:[Object(n.jsx)("option",{value:"sunny",children:"Sunny"}),Object(n.jsx)("option",{value:"half-shadow",children:"Half Shadow"}),Object(n.jsx)("option",{value:"shadow",children:"Shadow"})]}),Object(n.jsx)(v.a.Text,{className:"text-muted",children:"Please choose what exposition the plant needs"})]}),Object(n.jsxs)(v.a.Group,{children:[Object(n.jsx)(v.a.Label,{children:"Time to harvest"}),Object(n.jsx)(v.a.Control,{type:"text",name:"timeToHarvest",id:"timeToHarvest",value:c,onChange:this.handleChange,placeholder:"Enter days before harvest"}),Object(n.jsx)(v.a.Text,{className:"text-muted",children:"Please type the time in days after seeding to harvest the first vegetable"})]}),Object(n.jsx)("input",{type:"button",value:"Add",onClick:this.addForm})]})})}}]),a}(r.Component),g=function(e){Object(h.a)(a,e);var t=Object(d.a)(a);function a(){var e;Object(o.a)(this,a);for(var n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return(e=t.call.apply(t,[this].concat(r))).initialState={email:"",name:""},e.state=e.initialState,e.handleChange=function(t){var a=t.target,n=a.name,r=a.value;e.setState(Object(O.a)({},n,r))},e.submitForm=function(){e.props.sendInfo(e.state),e.setState(e.initialState)},e}return Object(l.a)(a,[{key:"render",value:function(){var e=this.state,t=e.email,a=e.name;return Object(n.jsx)(n.Fragment,{children:Object(n.jsxs)(v.a,{children:[Object(n.jsxs)(v.a.Group,{children:[Object(n.jsx)(v.a.Label,{children:"Email"}),Object(n.jsx)(v.a.Control,{type:"text",name:"email",id:"email",value:t,onChange:this.handleChange,placeholder:"Enter email"}),Object(n.jsx)(v.a.Text,{className:"text-muted",children:"Please type email"})]}),Object(n.jsxs)(v.a.Group,{children:[Object(n.jsx)(v.a.Label,{children:"Name"}),Object(n.jsx)(v.a.Control,{type:"text",name:"name",id:"name",value:a,onChange:this.handleChange,placeholder:"Enter name"}),Object(n.jsx)(v.a.Text,{className:"text-muted",children:"Please type name"})]}),Object(n.jsx)("input",{type:"button",value:"Submit",onClick:this.submitForm})]})})}}]),a}(r.Component),f=a(17),y=function(e){Object(h.a)(a,e);var t=Object(d.a)(a);function a(){var e;Object(o.a)(this,a);for(var n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return(e=t.call.apply(t,[this].concat(r))).state={characters:[],showPopup:!1},e.removeCharacter=function(t){var a=e.state.characters;e.setState({characters:a.filter((function(e,a){return a!==t}))})},e.handleSubmit=function(t){e.setState({characters:[].concat(Object(c.a)(e.state.characters),[t])})},e.sendInfo=function(t){var a=Object(c.a)(e.state.characters);if(null!=a)for(var n=0,r=a.length;n<r;n++)""!==a[n].seedingOutdoor[0]&&(a[n].seedingOutdoor=a[n].seedingOutdoor.map((function(e){return e.value}))),""!==a[n].seedingIndoor[0]&&(a[n].seedingIndoor=a[n].seedingIndoor.map((function(e){return e.value}))),""!==a[n].harvest[0]&&(a[n].harvest=a[n].harvest.map((function(e){return e.value})));console.log(JSON.stringify({email:t.email,name:t.name,info:"",seeds:a})),fetch("https://chefphan.com/gh-api/",{method:"POST",body:JSON.stringify({email:t.email,name:t.name,info:"",seeds:a}),headers:{"access-control-allow-origin":"*","Content-Type":"application/json"}}).then((function(e){return e.json()})).catch((function(e){return console.error("Error:",e)})).then((function(e){return console.log("Success:",e)})),e.setState({showPopup:!0,characters:[]})},e}return Object(l.a)(a,[{key:"togglePopup",value:function(){this.setState({characters:[],showPopup:!1})}},{key:"render",value:function(){var e=this.state.characters;return Object(n.jsxs)("div",{className:"container",children:[Object(n.jsx)(g,{sendInfo:this.sendInfo}),Object(n.jsxs)(f.a,{open:this.state.showPopup,children:[Object(n.jsx)("text",{children:"Table Submited "}),Object(n.jsx)("button",{onClick:this.togglePopup.bind(this),position:"center",children:"OK"})]}),Object(n.jsx)(b,{characterData:e,removeCharacter:this.removeCharacter}),Object(n.jsx)(p,{handleSubmit:this.handleSubmit})]})}}]),a}(r.Component);s.a.render(Object(n.jsx)(y,{}),document.getElementById("root"))}},[[28,1,2]]]);
//# sourceMappingURL=main.fcb4bf5f.chunk.js.map