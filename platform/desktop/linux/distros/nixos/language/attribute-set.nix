# the function receives an attribute set as argument
pkgs.mkShellNoCC {
  # the attribute "packages" is the result of filtering the "pkgs" attribute set picking only 2 items
  packages = with pkgs; [
    cowsay
    lolcat
  ];
}
