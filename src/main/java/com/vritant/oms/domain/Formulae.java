package com.vritant.oms.domain;

import com.fasterxml.jackson.annotation.JsonIgnore;

import org.hibernate.annotations.Cache;
import org.hibernate.annotations.CacheConcurrencyStrategy;

import javax.persistence.*;

import java.io.Serializable;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;
import java.util.Objects;
import java.util.SortedSet;
import java.util.TreeSet;

/**
 * A Formulae.
 */
@Entity
@Table(name = "formulae")
@Cache(usage = CacheConcurrencyStrategy.NONSTRICT_READ_WRITE)
public class Formulae implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @OneToMany(mappedBy = "parent")
    @JsonIgnore
    private Set<Formula> childrens = new HashSet<>();

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Set<Formula> getChildrens() {
        return childrens;
    }

    class FormulaComparator implements Comparator<Formula>{

        @Override
        public int compare(Formula arg0, Formula arg1) {
            return (int)(arg0.getId() - arg1.getId());
        }
    }

    @JsonIgnore
    public Set<Formula> getSortedChildrens() {
        SortedSet<Formula> result = new TreeSet<Formula>(new FormulaComparator());
        result.addAll(childrens);
        return result;
    }

    public void setChildrens(Set<Formula> formulas) {
        this.childrens = formulas;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Formulae formulae = (Formulae) o;
        if(formulae.id == null || id == null) {
            return false;
        }
        return Objects.equals(id, formulae.id);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(id);
    }

    @Override
    public String toString() {
        return "Formulae{" +
            "id=" + id +
            '}';
    }
}
