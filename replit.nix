{ pkgs }: {
  deps = [
    pkgs.libGLU
    pkgs.libGL
    pkgs.python39Full
    pkgs.ffmpeg
    pkgs.opencv
  ];
}