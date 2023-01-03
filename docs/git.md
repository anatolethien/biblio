# git

Utilisation du workflow [Gitflow](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow) pour gérer le repository.

![Gitflow](https://cdn-images-1.medium.com/max/1600/1*L0jHGLTJwZO5CTtpsn-dKA.png)

Passer sur la branche `dev`.

```git
git checkout dev
```

Créer une nouvelle branche 

```git
git checkout -b feature
```

Merge sur develop

```git
git checkout dev
git merge feature
```
