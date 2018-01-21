<?php
class equipe
{
    public $score_tours = array();
    public $equipe_name;
    public $equipe_pass;

    public function addScore($i, $score_tour){
//        $this->score_tours->add($i,$score_tour);
        array_push($score_tour, [$score_tour,$i]);
    }

    /**
     * @return array
     */
    public function getScoreTours()
    {
        return $this->score_tours;
    }

    /**
     * @param array $score_tours
     */
    public function setScoreTours($score_tours)
    {
        $this->score_tours = $score_tours;
    }

    /**
     * @return mixed
     */
    public function getEquipeName()
    {
        return $this->equipe_name;
    }

    /**
     * @param mixed $equipe_name
     */
    public function setEquipeName($equipe_name)
    {
        $this->equipe_name = $equipe_name;
    }

    /**
     * @return mixed
     */
    public function getEquipePass()
    {
        return $this->equipe_pass;
    }

    /**
     * @param mixed $equipe_pass
     */
    public function setEquipePass($equipe_pass)
    {
        $this->equipe_pass = $equipe_pass;
    }


}