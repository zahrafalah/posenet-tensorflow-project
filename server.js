//author: Zahra Falah
//CSC 535
//last update 6/30/22
//This file creates a express-node server and have a post request that uplods
//a video to server then execute some scripts to create a csv file for each video.

var express = require("express");
var fs = require("fs");
var app = express();
var bodyParser = require("body-parser");

const fileupload = require("express-fileupload");
const path = require("path");

app.use(fileupload());

const { execFile } = require("child_process");

app.use(bodyParser.json());

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

app.post("/upload", (req, res, next) => {
  const execute = async () => {
    try {
      console.log("received upload request");
      let fileName = "";
      let mimeType = "";
      let file = null;

      if (req.files) {
        file = req.files.videoname;
      }

      if (file) {
        fileName = file.name;
        mimeType = file.mimetype;
      }

      res.send({
        message: "File uploaded",
        fileName: fileName,
      });

      console.log('file: ', file);
      console.log("fileName: ", fileName);
      console.log("mimeType: ", mimeType);

      const videoName = fileName.split(".")[0];

      const time = new Date().getTime();

      let savepath = path.join(
        __dirname,
        "videos",
        "GESTURE_PRACTICE_" + req.body.username + "_" + time + "_" + videoName // videoFileName,  videoPath, "/"
      );

      if (!fs.existsSync(savepath)) {
        fs.mkdirSync(savepath);
      }

      const fullPathToVideo = savepath + "\\" + fileName;

      await file.mv(fullPathToVideo);

      console.log("full path to video", fullPathToVideo);

      savepath = savepath + "\\";

      execFile(
        "python",
        ["Frames_Extractor.py", savepath],
        (error, stdout, stderr) => {
          if (error || stderr) {
            // console.log("Frames error:", error);
            // console.log("Frames Std error:", stderr);
          }

          console.log(stdout);

          console.log("Executing key points.");
          const keypoints = savepath + videoName + "\\";
          execFile("node", ["main.js", keypoints], (err, stdout, stderr) => {
            if (err || stderr) {
              console.log("Key poinst err: ", err);
              console.log("Key points stderr: ", stderr);
            }

            console.log(stdout);

            console.log("Executing csv.");
            execFile(
              "python",
              ["convert_to_csv.py", keypoints],
              (err, stdout, stderr) => {
                if (err || stderr) {
                  console.log("csv stderr: ", stderr);
                  console.log("csv err: ", err);
                }

                console.log(stdout);

                // TODO: pass csv file to the location algorithm

                console.log("done");
              }
            );
          });
        }
      );
    } catch (e) {
      console.log(e);
    }
  };

  execute();

});

app.get("/*", (req, res, next) => {
  res.status(404).send();
});

const port = 3001;

app.listen(port);
console.log("Listening at port:  ", `${port}`);
