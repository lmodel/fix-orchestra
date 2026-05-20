package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class Repository  {

  private DctermsElementOrRefinementContainer metadata;
  private Categories categories;
  private Sections sections;
  private Datatypes datatypes;
  private CodeSets codeSets;
  private Fields fields;
  private Actors actors;
  private Components components;
  private Groups groups;
  private Messages messages;
  private Concepts concepts;
  private Scenarios scenarios;
  private String guid;
  private URI specUrl;
  private URI namespace;
  private String expressionLanguage;
  private Annotation annotation;
  private String name;
  private String version;


}