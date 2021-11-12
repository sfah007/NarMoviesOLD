(function () {
  var video = document.querySelector("#player");
  sourcesLength = document.getElementById("qualities").children.length
  defaultSource = document.getElementById("qualities").children[sourcesLength-1].children[0].innerHTML;
  if (Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource(defaultSource);
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED, function () {
      //video.play();
    });
  }
  plyr.setup(video);
})();


function switcher(url) {
  var video = document.querySelector("#player");
  if (Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource(url);
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED, function () {
      video.play();
    });
  }
}
