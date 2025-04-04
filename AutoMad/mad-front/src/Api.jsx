import axios from "axios";

export function getStories(setStories){
	axios.get("http://localhost:5000/stories").then((response) => {
		const stories = new Array();		
		Object.keys(response.data).forEach(function(key) {
			stories.push(response.data[key])
		});
		setStories(stories);
	}).catch((error) => {
      console.log(error);
    });
}

export function getStory(story, setStoryHTML, setShowStory){
	const formData = new FormData();
	formData.append("stories",story);
	const config = {
		headers: {
		  "content-type": "multipart/form-data",
		},
	};
	const url = "http://localhost:5000/story";
	axios.post(url, formData, config).then((response) => {
	setStoryHTML(response.data.story);
	setShowStory(true);
  })
    .catch((error) => {
      handleAxiosError(error, renderError);
    });
}

export function getFromText(story, sillyness, setStoryHTML, setShowStory){
	const formData = new FormData();
	formData.append("text", story);
	formData.append("sillyness", sillyness);
	const config = {
		headers: {
		  "content-type": "multipart/form-data",
		},
	};
	const url = "http://localhost:5000/text";
	axios.post(url, formData, config).then((response) => {
	setStoryHTML(response.data.story);
	setShowStory(true);
  })
    .catch((error) => {
      handleAxiosError(error, renderError);
    });
}

export function getPage(pageURL, sillyness, setStoryHTML, setShowStory){
	const formData = new FormData();
	formData.append("targetURL", pageURL);
	formData.append("sillyness", sillyness);
	const config = {
		headers: {
		  "content-type": "multipart/form-data",
		},
	};
	const url = "http://localhost:5000/renderPage";
	axios.post(url, formData, config).then((response) => {
		console.log(response);
		setStoryHTML(response.data.html);
		setShowStory(true);
  })
    .catch((error) => {
      handleAxiosError(error, renderError);
    });
}

export function saveStory(storyHTML){
	const url = "http://localhost:5000/storySaver";
	axios.post(url, {
	"story": storyHTML}).then((response) => {
		console.log(response);
  })
    .catch((error) => {
      handleAxiosError(error, renderError);
    });
}