//<div id="player"></div>
//<script src="https://www.youtube.com/iframe_api"></script>

        // Replace 'VIDEO_ID' with the ID of the YouTube video
        var videoId = 'tKCURAMFdd4';

        // Create a YouTube player
        var player;
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
                height: '315',
                width: '560',
                videoId: videoId,
                playerVars: {
                    'autoplay': 0, // Change to 1 for autoplay
                    'controls': 1,
                    'showinfo': 0,
                    'rel': 0,
                    'modestbranding': 1
                }
            });
        }