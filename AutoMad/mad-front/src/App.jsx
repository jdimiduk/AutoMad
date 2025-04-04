import {useEffect, useState } from 'react'
import {PrewrittenStories, PasteText, SillyPage, StoryDisplay} from './Components.jsx';
import {getStories} from './Api.jsx';
import './App.css'

function App() {
  const [stories, setStories] = useState(["loading stories"]);
  const [selectedStory, setSelectedStory] = useState();
  const [showStory, setShowStory] = useState(false);
  const [storyHTML, setStoryHTML] = useState("loading");

	useEffect(() => {
		getStories(setStories);
	}, []
	);
	

  return (
    <>{showStory ? <StoryDisplay setShowStory={setShowStory} storyHTML={storyHTML}/> :
      <div>
        Select a prewritten story:
			<PrewrittenStories stories={stories} selectedStory={selectedStory} setSelectedStory={setSelectedStory} 
								setShowStory={setShowStory} setStoryHTML={setStoryHTML}/>
			<PasteText setShowStory={setShowStory} setStoryHTML={setStoryHTML} />
			<SillyPage setShowStory={setShowStory} setStoryHTML={setStoryHTML} />
	</div>}
    </>
  )
}

export default App
