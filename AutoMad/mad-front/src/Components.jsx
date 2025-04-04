import {useState} from 'react'
import {getStory, getFromText, getPage, saveStory} from './Api.jsx';

export function PrewrittenStories({stories, selectedStory, setSelectedStory, setShowStory, setStoryHTML}){
	
	let handleStoryChange = (event) => {
		setSelectedStory(event.target.value);
	}
	
	return(
		<div>
		<select className="select select-bordered select-xs" onChange={handleStoryChange} value={selectedStory}>
            {stories.map((story, i) => <option key={i} value={story}>{story}</option>)}
        </select> 
		<button  className="btn btn-outline btn-sm" onClick={()=> getStory(selectedStory, setStoryHTML, setShowStory)}>Submit</button>
		</div>
	)
}

export function PasteText({setShowStory, setStoryHTML}){	
	const [pastedText, setPastedText] = useState();
	const [sillyness, setSillyness] = useState(33);
	
	let handleTextChange = (event) => {
		setPastedText(event.target.value);
	}
	
	let handleSillyChange = (event) => {
		setSillyness(event.target.value);
	}
	
	return(
	<div>
	<textarea className="textarea" placeholder="Paste text here"  onChange={handleTextChange} value={pastedText}></textarea>
	<input type="range" min={0} max="100" className="range" onChange={handleSillyChange} value={sillyness}></input>
	<button  className="btn btn-outline btn-sm" onClick={()=> getFromText(pastedText, sillyness, setStoryHTML, setShowStory)}>Submit</button>
	</div>
	)
}

export function SillyPage({setShowStory, setStoryHTML}){
	const [url, setUrl] = useState();
	const [sillyness, setSillyness] = useState(33);
	
	let handleTextChange = (event) => {
		setUrl(event.target.value);
	}
	
	let handleSillyChange = (event) => {
		setSillyness(event.target.value);
		console.log(pageHTML);
	}
	
	function getPageFromAPI(url, sillyness, setPageHTML){
		getPage(url, sillyness, setPageHTML);
		setStoryHTML(pageHTML);
		setShowStory(true);
	}
	
	
	return(
	<div>
	<textarea className="textarea" placeholder="Paste text here"  onChange={handleTextChange} value={url}></textarea>
	<input type="range" min={0} max="100" className="range" onChange={handleSillyChange} value={sillyness}></input>
	<button  className="btn btn-outline btn-sm" onClick={()=> getPageFromAPI(url, sillyness, setStoryHTML, setShowStory)}>Submit</button>
	</div>
	)
}

export function StoryDisplay({storyHTML, setShowStory}){
	
	function createMarkup(){
        return {__html: storyHTML};
    }
	return(
	<div>
	 <button  className="btn btn-outline btn-sm" onClick={()=> setShowStory(false)}>Back</button>
	 <button  className="btn btn-outline btn-sm" onClick={()=> saveStory(storyHTML)}>Save</button>
	 <div dangerouslySetInnerHTML={createMarkup()}/>
	 </div>
	 )
}